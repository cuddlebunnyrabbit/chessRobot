from chess import *
#import os
#import chess.pgn
#import lcd_main as lcd

from log import *
import speech_recognition as sr
import chess.engine 

from phrase import *
from parser import *

class Daemon:
    def __init__(self):
        self.r = sr.Recognizer()
        self.l = Log()
        self.listening = True
        self.gameOn = True
        self.review = False
        self.engine = False
        self.side = None

        while self.listening:
            data = self.listen()
            print("data: ", data)

            if self.gameOn and self.engine != False:
                if self.side != self.l.getNextColor(): #if i am playing white and the mv rn black
                    result = self.engine.play(self.l.board, chess.engine.Limit(time=0.1))
                    self.l.makeMove(result.move.uci())
                    self.l.getFullStatus()

            if data != None:
                #checks if you have key command
                command = parse(cleanData(data))
                print("This is what I parsed:", command)

                if command in key_phrase:
                    self.checkKeyPhrase(command)

                else:
                    if self.gameOn and self.review == False: #when it is game on and not during review
                        if command != None:
                            if self.engine != False:
                                if self.side == self.l.getNextColor():
                                    self.l.makeMove(command)
                                    self.l.getFullStatus()
                            else:
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
        
            if self.l.game.next() != None:
                self.l.export()
                self.l.restart_game()

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
                self.engine = False
                self.side = None

        elif phrase == "spectate":
            if self.review == False: 
                pgn = "kasparov_topalov_1999.pgn"
                self.review = self.l.get_review_iter(pgn)
        
        elif phrase == "review": # implement this thing 
            if self.review == False: 
                pgn = "export.pgn"
                self.review = self.l.get_review_iter(pgn)

        elif phrase == "blackengine":
            self.engine = chess.engine.SimpleEngine.popen_uci(r"/usr/local/Cellar/stockfish/15/bin/stockfish")
            if self.side == None:
                self.side = "B"
            else:
                print("terminate or reset this game before changing engine")

        elif phrase == "whiteengine":
            self.engine = chess.engine.SimpleEngine.popen_uci(r"/usr/local/Cellar/stockfish/15/bin/stockfish")
            if self.side == None:
                self.side = "W"
            else:
                print("terminate this game before changing engine")

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