from chess import *
#import os
#import chess.pgn
#import displaycode.lcd_main as lcd

from log import *
import speech_recognition as sr

from phrase import *
from parser import *

#from pocketsphinx import LiveSpeech, get_model_path

class Daemon:
    def __init__(self):
        self.r = sr.Recognizer()
        self.l = Log()
        self.listening = True
        self.gameOn = True

        self.review = False

        # when the button is pushed 
# need button integration 
        while self.listening:
            data = self.listen()

            if data != None:
                #checks if you have key command
                command = parse(cleanData(data))
                print("This is what I parsed:", command)
                if command in key_phrase:
                    self.checkKeyPhrase(command)

                else:
                    if self.gameOn and self.review == False: #when it is game on and not during review
                        print(" I am in self.gameON")
                        if self.review == False:
                            if command != None:
                                self.l.makeMove(command)
                                self.l.getFullStatus()

            if self.review != False: # if the self is reviewing a game
                print("I am in reviewing mode")
                nextmv = next(self.review)
                print("nextmv: ", nextmv)
                self.l.makeMove(str(nextmv))
                #self.l.getFullStatus()
                        
            #else:
                #print("No data you gotta try again")

    def checkKeyPhrase(self, phrase):
        if phrase == "terminate": #if i hear terminate
            #lcd.printMessage(["Terminated", "Game"])
            self.gameOn = False
            self.review = False
            self.listening = False
            print("I have terminated the game. stopped listening. game is off.")

        elif phrase == "resign": #no added protection for resign game yet! needs more implementation
            pass
            self.gameOn = False

        elif phrase == "resume": 
            self.l.getFullStatus()
            self.gameOn = True
            #lcd.printMessage(["Resume Game", self.l.getCondensedStatus()])

        elif phrase == "pause":
            self.l.getFullStatus()
            self.gameOn = False
            #lcd.printMessage(["Paused Game", self.l.getCondensedStatus()])

        elif phrase == "reset":
            if self.gameOn:
                lcd.printMessage(["Game in progress", "Terminate game?"])

            else:
                #you need to go through and generate the coordinates map
                ...
                #lcd.printMessage(["Reseting Game","Plz be patient"])

        elif phrase == "play":
            #print("I got into play in checkkeyphrase")
            pgn = open("kasparov_topalov_1999.pgn")
            self.review = chess.pgn.read_game(pgn).mainline_moves()
            self.review = iter(self.review) 
            #converts the moves into an iteraboe object then we can do thru one by one

    def listen(self):
        with sr.Microphone() as source:
            print('Speak Anything:')
            audio = self.r.listen(source)

            try:
                data = self.r.recognize_google(audio)#convert audio to text
                print('I Heard: {}'.format(data))
                return data

            except:
                print('Sorry could not recognize your voice')
                return None

d = Daemon()

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