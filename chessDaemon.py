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
            #data = self.listen()

            if data != None:
                #checks if you have key command
                command = parse(cleanData(data))
                print("This is what I parsed:", command)
                if command in key_phrase:
                    self.checkKeyPhrase(command)

                else:
                    #print("I am in the else loop")
                    if self.gameOn and self.review == False: #when it is game on and not during review
                        #print(" I am in self.gameONnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
                        if command != None:
                            #print("I am attempting to make moves at this pt")
                            self.l.makeMove(command)
                            self.l.getFullStatus()
                        else:
                            print("command is none?")

            if self.gameOn and self.review != False: # if the self is reviewing a game
                print("I am in reviewing mode")
                try:
                    nextmv = next(self.review)
                    self.l.makeMove(str(nextmv))
                    self.l.getFullStatus()
                except:
                    print("ran out of moves lol")

    def checkKeyPhrase(self, phrase):
        if phrase == "terminate": #if i hear terminate
            #lcd.printMessage(["Terminated", "Game"])
            self.gameOn = False
            self.review = False
            self.listening = False

            #print("before termination of game: ", self.l.game)
        
            if self.l.game.next() != None:
                self.l.export()
                self.l.restart_game()
            #print("I have terminated the game. stopped listening. game is off.")

        elif phrase == "resign": #no added protection for resign game yet! needs more implementation
            pass
            self.gameOn = False

        elif phrase == "resume": 
            self.l.getFullStatus()
            self.gameOn = True
            #lcd.printMessage(["Resume Game", self.l.getCondensedStatus()])

        elif phrase == "pause":
            #self.l.getFullStatus()
            self.gameOn = False
            print("I have paused the game yoooo! waitin to resume again")
            #lcd.printMessage(["Paused Game", self.l.getCondensedStatus()])

        elif phrase == "reset":
            if self.gameOn:
                print("game in progress, pause game first?")
                #lcd.printMessage(["Game in progress", "Terminate game?"])
            else:
                #lcd.printMessage(["Reseting Game","Plz be patient"])
                self.l.reset()
                self.review = False #stops reviewing

        elif phrase == "spectate":
            if self.review == False: 
                pgn = "kasparov_topalov_1999.pgn"
                self.review = self.l.get_review_iter(pgn)
        
        elif phrase == "review": # implement this thing 
            if self.review == False: 
                pgn = "export.pgn"
                self.review = self.l.get_review_iter(pgn)

        elif phrase == "engine":
            print("you still must implement the engine function")

            #converts the moves into an iteraboe object then we can do thru one by one

    def listen(self):
        with sr.Microphone() as source:
            print('Speak Anything:')

            audio = None
            TIME_LIMIT = 5
            
            try: 
                audio = self.r.listen(source, TIME_LIMIT, phrase_time_limit= TIME_LIMIT)

                try:
                    print("recognizing......")
                    data = self.r.recognize_google(audio)#convert audio to text
                    #print('I Heard: {}'.format(data))
                    return data

                except:
                    print('Sorry could not recognize your voice')
                    return None
            except:
                return None

d = Daemon()