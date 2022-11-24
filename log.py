import chess
import chess.pgn
#from MotorCode import *
from shadowRealm import *

class Log:
    def __init__(self):
        self.game = chess.pgn.Game()
        self.node = None
        self.board = chess.Board()

    #san() gets the algebranic notation to the node!
    # you can find all the errors the machine can throw 
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

    def makeMove(self, move):
        currmove = chess.Move.from_uci(move)

        if currmove in self.board.legal_moves:
            self.motorMove(move) #do not continue until motorMove has terminated! 
            if self.node == None: #fist move
                
                self.node = self.game.add_variation(currmove)

            else:
                self.node = self.node.add_variation(currmove)

            self.board.push_uci(move) 
        else:
            print("invalid or illegal move! try again plz")

    def getTurn(self): #increments after black moves. starts at 1
        return self.board.fullmove_number

    def getCondensedStatus(self):
        return "Next Move:", self.getTurn(), ".", self.getNextColor()

    def getFullStatus(self): #helper method for chessDaemon
        print(self.getGame())
        print(self.getBoard())

    def getGameStatus(self):
        return #who won the game?

    def getBoard(self): #maybe jerry could use this?
        return self.board

    def getGame(self):
        return self.game

    #helpter methods used by motormove!
    def getPiece(self, location): #location should be d5 for example
        square_name = chess.parse_square(location)
        piece = self.board.piece_at(square_name)
        return piece #returns Q or q! 

    #motorMove: that may interact with shadowrealm and give motor code info 
    def motorMove(self, move):
        origin = move[:2]
        destination = move[2:4] #check your assumptions! not allways will be string be 4!
        currmove = chess.Move.from_uci(move)

        if self.board.is_capture(currmove) and not self.board.is_en_passant(currmove): 
            print("this is a normal capture: ", (destination, self.getPiece(destination)))
            #NOTE: SELF.GETPIECE IS SHOWN AS "P" OR LOWERCASE 
            # BUT IT IS A PIECE OBJECT NOT A STRING

            #shadowRealm.banash(destination, self.getPiece(destination)) 
            #banash should be current location, piece

        if self.getPiece(origin) == "N" or self.getPiece(origin) == "n":
            print("this is a knight move: ", (origin, destination, True))
            #MotorCode.push_move(origin, destination, True)

        elif self.board.is_castling(currmove):
            print("this is a castle: ", (origin, destination, False))
            #MotorCode.push_move(origin, destination, False) #move the king normally  

            if destination[0] == "c": #move the rook abnormally
                print("accompaning rook move: ," ("a" + destination[1], "d" + destination[1], True))
                #MotorCode.push_move("a" + destination[1], "d" + destination[1], True) 
            else:
                print("accompaning rook move: ," ("h" + destination[1], "f" + destination[1], True))
                #MotorCode.push_move("h" + destination[1], "f" + destination[1], True)

        elif self.board.is_en_passant(currmove):
            capturedpawnloc = destination[0] + origin[1] #move the piece normally
            #MotorCode.push_move(origin, destination, False) 
            #shadowRealm.banash(capturedpawnloc, self.getPiece(capturedpawnloc)) #move the shadowrealm
            print("this is en_passant 1st move motor code: ", (origin, destination, False))
            print("this is en_passant 2nd move shadowbanish: ", (capturedpawnloc, self.getPiece(capturedpawnloc)))
            
        else: #under a normal move
            print("this is a normal move: ", (origin, destination, False))
            #MotorCode.push_move(origin, destination, False)

            if len(move) == 5: #if the move is a promotion move
                promotion_piece = move[-1]
                #shadowRealm.banash(destination, self.getPiece(destination))
                #shadowRealm.reinstate(destination, promotion_piece)
                print("this is a promotion: ", promotion_piece)
                print("promotion: shadow banaish", (destination, self.getPiece(destination)))
                print("shadowretrieving: ", (destination, promotion_piece))
        
#the e1g1 will give the castling! you will not need anything else 


l = Log()
l.makeMove("e2e4")
l.makeMove("f7f5")
l.makeMove("e4e5")
l.makeMove("d7d5")
l.makeMove("e5d6")
l.makeMove("e7e5")
l.makeMove("d6c7")
l.makeMove("f8b4")
l.makeMove("c7b8q")
l.makeMove("g8e7")
l.makeMove("d1f3")
l.makeMove("e8g8")

'''
print(l.getBoard())
print(l.getGame())
print(l.getTurn())
print(l.getCondensedStatus())
'''




