import chess
from speechTester.commandInterpreter import *

# when the button is pushed 
#need button integration 

gameOn = True

board = chess.Board()
board.legal_moves
chess.Move.from_uci("a8a1") in board.legal_moves

while gameOn:
    # open microphone + listen to the data 
    data = ...
    command = parse(cleanData(data))

    
    
    if ...: #if i hear terminate
        gameOn = False

def interpretX(): #parser only cleans data. gameOn will interpret + resolve issues
    if (command[0] == "x"): 
        pass
        #check if white or black to move 
        #if white to move, check the 2 squares if they have pawns 
        #change results accordingly

def logGame():
    pass
