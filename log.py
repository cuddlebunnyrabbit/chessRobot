import chess
import chess.pgn

game = chess.pgn.Game()
node = None

board = chess.Board()

#san() gets the algebranic notation to the node!
# you can find all the errors the machine can throw 
def getNextColor():
    #node.turn() returns the true if the next move is white 
    #node.turn() returns false if the next move is black
    try:
        if node.turn():
            return "W"
        return "B"
    except: 
        if game.turn():
            return "W"
        return "B"

def makeMove(move):
    try: 
        node = node.add_variation(chess.Move.from_uci(move))
        board.push_san(move)
    except UnboundLocalError:
        node = game.add_variation(chess.Move.from_uci(move))
        board.push_san(move)
    except: 
        print("Unknown error! try again")
    
def getTurn(): #increments after black moves. starts at 1
    return board.fullmove_number

def getCondensedStatus():
    return "Next Move:", getTurn(), ".", getNextColor()

def getGameStatus():
    return #who won the game?

def getBoard():
    return board

def getGame():
    return game


        #print(getNextMove())
#makeMove("e2e4")
#print(getTurn())
#print(board.push_san("e2e4"))
#print(board)
#print(game)