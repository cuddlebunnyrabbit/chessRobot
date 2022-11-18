import chess
import chess.pgn


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
        if self.node == None:
            print("UnboundLocalError! Add first move to game! ")
            try:
                #must have push_uci before the node since try will execute all 
                #commands until it reaches a bad thing and then it suddenly stopps,
                #leaving the command 1/2 executed and corrupting the data
                self.board.push_uci(move) 
                self.node = self.game.add_variation(chess.Move.from_uci(move))
            except:
                print("invalid or illegal move. try again")

        else:
            print("Normal move")
            try:
                self.board.push_uci(move)
                self.node = self.node.add_variation(chess.Move.from_uci(move))
            except:
                print("invalid or illegal move. try again")
            #You gotta check these moves to see if they are valid with try and except 
        
    def getTurn(self): #increments after black moves. starts at 1
        return self.board.fullmove_number

    def getCondensedStatus(self):
        return "Next Move:", self.getTurn(), ".", self.getNextColor()

    def getGameStatus(self):
        return #who won the game?

    def getBoard(self):
        return self.board

    def getGame(self):
        return self.game

    #helper method for chessDaemon
    def getFullStatus(self):
        print(self.getGame())
        print(self.getBoard())


#the e1g1 will give the castling! you will not need anything else 

'''
l = Log()
l.makeMove("e2e4")
l.makeMove("d7d5")
l.makeMove("e4d5")
l.makeMove("c7c6")
l.makeMove("d5c6")
l.makeMove("c8g4")
l.makeMove("c6b7")
l.makeMove("f7f6")
l.makeMove("b7a8q")
print(l.getBoard())
print(l.getGame())
print(l.getTurn())
print(l.getCondensedStatus())
'''



