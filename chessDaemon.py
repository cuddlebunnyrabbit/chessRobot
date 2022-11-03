import chess
import os
import sys
sys.path.append("/Users/kerryhuang/Documents/chessRobot/speechTester/")
print(sys.path)
#import displaycode.lcd_main as lcd

from log import *
import speech_recognition as sr

#from speechTester.phrase import *
from parser import *

from pocketsphinx import LiveSpeech, get_model_path


# when the button is pushed 
#need button integration 
r = sr.Recognizer()
listening = True
gameOn = True


def getFullStatus():
    print(getGame())
    print(getBoard())

def checkKeyPhrase(phrase):
    if phrase == "terminate": #if i hear terminate
        lcd.printMessage(["Terminated", "Game"])
        gameOn = False
        listening = False
        return False

    elif phrase == "resign": #no added protection for resign game yet!
        pass
        gameOn = False
        return False

    elif phrase == "resume":
        getFullStatus()
        lcd.printMessage(["Resume Game", getCondensedStatus()])
        gameOn = True
        return False

    elif phrase == "pause":
        getFullStatus()
        gameOn = False
        lcd.printMessage(["Paused Game", getCondensedStatus()])

    elif phrase == "reset":
        if gameOn:
            lcd.printMessage(["Game in progress", "Terminate game?"])

        else:
            lcd.printMessage(["Reseting Game","Plz be patient"])

    return True

while listening:
    data = None
    with sr.Microphone() as source:
        print('Speak Anything:')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)#convert audio to text
            print('You said: {}'.format(text))
            data = text

        except:
            print('Sorry could not recognize your voice')
    
    command = parse(cleanData(data))
    try:
        checkKeyPhrase(command)
        makeMove(command)
        getFullStatus()
    except:
        print("lol no action is done")
    
#every time at the end you print game and board 
getFullStatus()



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