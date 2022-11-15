from chess import *
#import os
#import chess.pgn
#import displaycode.lcd_main as lcd

from log import *
import speech_recognition as sr

from phrase import *
from parser import *

from pocketsphinx import LiveSpeech, get_model_path

# when the button is pushed 
#need button integration 
r = sr.Recognizer()
l = Log()

def checkKeyPhrase(phrase):
    if phrase == "terminate": #if i hear terminate
        lcd.printMessage(["Terminated", "Game"])
        gameOn = False
        listening = False

    elif phrase == "resign": #no added protection for resign game yet! needs more implementation
        pass
        gameOn = False

    elif phrase == "resume":
        l.getFullStatus()
        lcd.printMessage(["Resume Game", getCondensedStatus()])
        gameOn = True

    elif phrase == "pause":
        l.getFullStatus()
        gameOn = False
        lcd.printMessage(["Paused Game", getCondensedStatus()])

    elif phrase == "reset":
        if gameOn:
            lcd.printMessage(["Game in progress", "Terminate game?"])

        else:
            lcd.printMessage(["Reseting Game","Plz be patient"])

    elif phrase == "play":
        pgn = open("kasparov_topalov_1999.pgn")
        review = pgn

def listen():
    with sr.Microphone() as source:
        print('Speak Anything:')
        audio = r.listen(source)

        try:
            data = r.recognize_google(audio)#convert audio to text
            print('I Heard: {}'.format(data))
            return data

        except:
            print('Sorry could not recognize your voice')
            return None


listening = True
gameOn = True
review = False

while listening:
    data = listen()
    
    if data != None:
        command = parse(cleanData(data))
        print("This is what I parsed:", command)

        if command in key_phrase:
            checkKeyPhrase(command)

        else:
            if command == None:
                ...
                print("waiting a response")

            else:
                l.makeMove(command)
                l.getFullStatus()

    else:
        print("No data you gotta try again")

    #command could be 
    '''
    nonsense word
    keyphrase
    actual move 
    '''

    '''
    try:
        checkKeyPhrase(command)
        if gameOn == True:
            if review == False:
                makeMove(command)
            else:
                makeMove(review.mainline_moves())
        else:
            print("waiting to resume")
        
        getFullStatus()

    except:
        print("lol no action is done")
    '''
    
#every time at the end you print game and board 
l.getFullStatus()



'''
# add if you still got time 
def interpretX(): #parser only cleans data. gameOn will interpret + resolve issues
    pass
    if (command[0] == "x"): 
        pass
        #check if white or black to move 
        #if white to move, check the 2 squares if they have pawns 
        #change results accordingly
'''