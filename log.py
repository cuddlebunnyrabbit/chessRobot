import chess
import chess.pgn
from shadowRealm import *
from chess.engine import *
import led as led
import lcd_main as lcd
import motorlib

class Log:
    def __init__(self):
        self.game = chess.pgn.Game()
        self.node = None
        self.board = chess.Board()
        self.shadow = shadowRealm()
        
        W_PAWN = ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']
        W_ROOK = ['a1', 'h1']
        W_KNIGHT = ['b1', 'g1']
        W_BISHOP = ['c1', 'f1']
        W_QUEEN = ['d1']
        W_KING = ['e1']

        B_PAWN = ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']
        B_ROOK = ['a8', 'h8']
        B_KNIGHT = ['b8', 'g8']
        B_BISHOP = ['c8', 'f8']
        B_QUEEN = ['d8']
        B_KING = ['e8']

        self.constants_dict = {
            'P': W_PAWN,
            'R': W_ROOK,
            'N': W_KNIGHT,
            'B': W_BISHOP,
            'Q': W_QUEEN,
            'K': W_KING,
            'p': B_PAWN,
            'r': B_ROOK,
            'n': B_KNIGHT,
            'b': B_BISHOP,
            'q': B_QUEEN,
            'k': B_KING,
        }
        
        

    
    def makeMove(self, move): #make a normal move or review 

        currmove = chess.Move.from_uci(move)
        if currmove in self.board.legal_moves: 
            led.blue()
            self.motorMove(move) #do not continue until motorMove has terminated! 
            if self.node == None: #fist move
                self.node = self.game.add_variation(currmove)
            else:
                self.node = self.node.add_variation(currmove)
            self.board.push_uci(move) 
        else:
            lcd.printMessage(["Illegal move", "Try again"])
            led.red()

    def get_review_iter(self, pgn): #helper method to get the iter for review and spectate
        temp = chess.pgn.read_game(open(pgn)).mainline_moves()
        temp = iter(temp)
        return temp

    #helpter methods used by motormove!
    def getPiece(self, location): #location should be d5 for example
        square_name = chess.parse_square(location)
        piece = self.board.piece_at(square_name)
        if piece:
            return piece.symbol()
        return None #returns Q or q! 


    ########### helper methods for reset 
    def find_storage(self, currloc): #should give the temp storage of a piece 
        for rank in [3, 4, 5, 6]:
            file = currloc[0]
            square = file + str(rank)
            #print(square)
            if not self.getPiece(square):
                return square
        
        for rank in [3, 4, 5, 6]:
            for file in chess.FILE_NAMES:
                square = file + str(rank)
                if not self.getPiece(square):
                    return square

    def find_home(self, piece): #returns the location that the piece should be stored in permenently
        home = self.constants_dict[piece]
        for loc in home:
            occupying_piece = self.getPiece(loc)
            if not occupying_piece: #if there is an occupying piece
                return loc
        return None

    def clean_house(self): #returns a clean 1, 2, 7, 8 ranks 
        for rank in [1, 2, 7, 8]:
            #print("----------------------------------------------------- rank", rank)
            for file in chess.FILE_NAMES:
                location = file + str(rank)
                piece = self.getPiece(location)
                if not piece: #if the piece is None
                    pass
                    #print(location, piece, "empty")
                elif location in self.constants_dict[piece]: #if the piece is correctly placed
                    pass
                    #print(location, piece, "correct")
                else:
                    home = self.find_home(piece)
                    if home:
                        self.motorReset(location + home)
                        #print("I found my home at ", home, "while i am currently at ", location)
                    else:
                        storage = self.find_storage(location)
                        self.motorReset(location + storage)
                        #print("I found temp storage location at ", storage, "while i am currently at ", location)
    def reset(self): #reset your own board before you reset the other board 
        self.clean_house()

        for rank in [3, 4, 5, 6]:
            for file in chess.FILE_NAMES:
                location = file + str(rank)
                piece = self.getPiece(location)
                if piece:
                    home = self.find_home(piece)
                    self.motorReset(location + home)
                    self.getFullStatus()

        for row in self.shadow.board.ROW:
            for col in self.shadow.board.COLUMN:
                location = col + str(row)
                piece = self.shadow.board.get(location)
                if piece:
                    home = self.find_home(piece)
                    self.motorReset(location + home)
                    self.getFullStatus()

        self.export()
        self.restart_game()
        #restart the game from new 
    #helper methods for reset 

    #methods for motor in diff conditions
    def motorReset(self, move): # this is used to move the pieces during resets
        origin = move[:2]
        destination = move[2:4]
        piece = None

        motorlib.MotorSys.push_move(origin, destination, True)
        if origin[0] in self.shadow.board.COLUMN: #if the shadowboard is involved
            piece = self.shadow.board.empty_square(origin)
            sq = chess.parse_square(destination)
            pieceThing = chess.Piece.from_symbol(piece)
            self.board.set_piece_at(sq, pieceThing)
            
        else:
            piece = self.getPiece(origin)
            original_sq = chess.parse_square(origin)
            self.board.remove_piece_at(original_sq)
            destination_sq = chess.parse_square(destination)
            pieceThing = chess.Piece.from_symbol(piece)
            self.board.set_piece_at(destination_sq, pieceThing)

    #motorMove: this is used to make a normal move under normal circumstances like play and engine play
    def motorMove(self, move):
        origin = move[:2]
        destination = move[2:4] #check your assumptions! not always will be string be 4!
        currmove = chess.Move.from_uci(move)
        

        if self.board.is_capture(currmove) and not self.board.is_en_passant(currmove):
            lcd.printMessage(["Capture:" + move,self.getCondensedStatusCurrent()])
            self.shadow.banash(self.getPiece(destination), destination)
            print("this is a normal capture: ", (destination, self.getPiece(destination)))
            #NOTE: SELF.GETPIECE IS SHOWN AS "P" OR LOWERCASE 
            # BUT IT IS A PIECE OBJECT NOT A STRING

        if self.getPiece(origin) == "N" or self.getPiece(origin) == "n":
            print("this is a knight move: ", (origin, destination, True))
            motorlib.MotorSys.push_move(origin, destination, True)

        elif self.board.is_castling(currmove):
            lcd.printMessage(["Castleing:",self.getCondensedStatusCurrent()])
            print("this is a castle: ", (origin, destination, False))
            motorlib.MotorSys.push_move(origin, destination, False) #move the king normally  

            if destination[0] == "c": #move the rook abnormally
                print("accompaning rook move: ", ("a" + destination[1], "d" + destination[1], True))
                motorlib.MotorSys.push_move("a" + destination[1], "d" + destination[1], True) 
            else:
                print("accompaning rook move: ", ("h" + destination[1], "f" + destination[1], True))
                motorlib.MotorSys.push_move("h" + destination[1], "f" + destination[1], True)

        elif self.board.is_en_passant(currmove):
            capturedpawnloc = destination[0] + origin[1] #move the piece normally
            motorlib.MotorSys.push_move(origin, destination, False) 
            coordinate = self.shadow.banash(self.getPiece(capturedpawnloc), capturedpawnloc) #move the shadowrealm
            
            print("this is en_passant 1st move motor code: ", (origin, destination, False))
                
        else: #under a normal move
            lcd.printMessage(["Move:" + move,self.getCondensedStatusCurrent()])
            print("this is a normal move: ", (origin, destination, False))
            print(type(origin))
            motorlib.MotorSys.push_move(origin, destination, False)

            if len(move) == 5: #if the move is a promotion move
                promotion_piece = str(move[-1])
                if int(move[-2]) == 8: #if the move is a white move
                    promotion_piece = promotion_piece.upper()
                shadowRealm.banash(self.getPiece(destination), destination)
                shadowRealm.reinstate(promotion_piece, destination)
                print("this is a promotion: ", promotion_piece)
                self.shadow.reinstate(promotion_piece)
    #methods for motor in diff conditions 


    def export(self): #methods for outside daemon and also for reset  
        print(self.game, file=open("export.pgn", "w"), end="\n\n")
        print(self.game, file=open("export_log.pgn", "a"), end="\n\n")   

    def restart_game(self): #used by reset as well as other functions
        self.game = chess.pgn.Game()
        self.board = chess.Board()
        self.node = None


    #communicates with lcd 
    def getNextColor(self):
        #node.turn() returns the true if the next move is white 
        #node.turn() returns false if the next move is black
        try:
            if self.node.turn():
                return "W"
            return "B"
        except: 
            if self.game.turn():
                return "W"
            return "B"

    def getTurn(self): #increments after black moves. starts at 1
        return str(self.board.fullmove_number)

    def getCondensedStatusCurrent(self):
        return "Current Move:" + self.getTurn() + "." + self.getNextColor()
    
    def getCondensedStatusNext(self):
        return "Next Move:" + self.getTurn() + "." + self.getNextColor()

    def getFullStatus(self): #helper method for chessDaemon
        print(self.shadow.board)
        print(self.getGame())
        print(self.getBoard())

    #def getGameStatus(self):
        #return #who won the game?

    def getBoard(self):
        return self.board

    def getGame(self):
        return self.game


'''
l = Log()
pgn = open("kasparov_topalov_1999.pgn")
review = chess.pgn.read_game(pgn).mainline_moves()
review = iter(review)

for thing in review:
    l.makeMove(str(thing))

l.export()
'''
