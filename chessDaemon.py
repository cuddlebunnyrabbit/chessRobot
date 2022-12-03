from chess import *
#import os
#import chess.pgn
#import lcd_main as lcd

from log import *
import speech_recognition as sr
import chess.engine 

from phrase import *
from parser import *
import led as led

import os

#daemon runs listing loop when activated
class Daemon:
    def __init__(self):
        self.r = sr.Recognizer()
        self.l = Log()
        self.listening = True
        self.gameOn = True
        self.review = False
        self.engine = False
        self.side = None

        #while not terminated, always listening
        while self.listening:
            led.green()
            data = self.listen()
            print("data: ", data)

            if self.gameOn and self.engine != False:
                #if i am playing white and the mv rn black
                if self.side != self.l.getNextColor(): 
                    led.blue()
                    result = self.engine.play(self.l.board, chess.engine.Limit(time=0.1))
                    self.l.makeMove(result.move.uci())
                    self.l.getFullStatus()

            if data != None:
                command = parse(cleanData(data))
                #print("This is what I parsed:", str(command))
                if command in key_phrase: #checks if you have key command
                    led.flashing()
                    self.checkKeyPhrase(command)
                else:
                     #when it is game on and not during review
                    if self.gameOn and self.review == False:
                        if command != None:
                            if self.engine != False:
                                if self.side == self.l.getNextColor():
                                    led.blue()
                                    self.l.makeMove(command)
                                    self.l.getFullStatus()
                            else:
                                led.blue()
                                self.l.makeMove(command)
                                self.l.getFullStatus()
                        else:
                            led.blue()
                            
            if self.gameOn and self.review != False:  # if the self is reviewing a game
                try:
                    nextmv = next(self.review)
                    self.l.makeMove(str(nextmv))
                    self.l.getFullStatus()
                except:
                    lcd.printMessage(["Depleted", "Game"])

    #input: String(phrase) determinds the action related for each key phrase
    def checkKeyPhrase(self, phrase):
        if phrase == "terminate": #if i hear terminate
            lcd.printMessage(["Terminated", "Game"])
            self.gameOn = False
            self.review = False
            self.listening = False
        
            if self.l.game.next() != None:
                self.l.export()
                self.l.restart_game()

        elif phrase == "resume": 
            lcd.printMessage(["Resume Game", self.l.getCondensedStatusNext()])
            self.l.getFullStatus()
            self.gameOn = True
            
        elif phrase == "pause":
            self.gameOn = False
            lcd.printMessage(["Paused Game", self.l.getCondensedStatusNext()])
            
        elif phrase == "reset":
            if self.gameOn:
                led.red()
                lcd.printMessage(["Game in progress", "Terminate game?"])
                print("Game in progress, pause game first?")
                
            else:
                led.blue()
                lcd.printMessage(["Reseting Game","Plz be patient"])
                self.l.reset()
                self.review = False #stops reviewing
                self.engine = False
                self.side = None

        elif phrase == "spectate":
            if self.review == False: 
                pgn = "kasparov_topalov_1999.pgn"
                self.review = self.l.get_review_iter(pgn)
            else:
                lcd.printMessage(["Error:", "Already reviewing"])
                led.red()
                print("game in progress, pause game first?")
        
        elif phrase == "review": 
            if self.review == False: 
                pgn = "export.pgn"
                self.review = self.l.get_review_iter(pgn)
            else:
                lcd.printMessage(["Error:", "Already reviewing"])
                led.red()

        elif phrase == "blackengine":
            self.engine = chess.engine.SimpleEngine.popen_uci(r"/usr/games/stockfish")
            if self.side == None:
                self.side = "B"
            else:
                lcd.printMessage(["Error:", "Engine in progress"])
                led.red()
                
        elif phrase == "whiteengine":
            self.engine = chess.engine.SimpleEngine.popen_uci(r"/usr/games/stockfish")
            if self.side == None:
                self.side = "W"
            else:
                lcd.printMessage(["Error:", "Engine in progress"])
                led.red()

    #listen to all inputs and controls the lights accordingly
    def listen(self):
        with sr.Microphone(sample_rate = 16000) as source:
            print('Speak Anything:')
            led.green()
            audio = None
            TIME_LIMIT = 5
            try:
                self.r.energy_threshold = 1000
                self.r.adjust_for_ambient_noise(source)
                audio = self.r.listen(source, TIME_LIMIT, phrase_time_limit= TIME_LIMIT)
                try:
                    print("recognizing......")
                    led.blue() 
                    data = self.r.recognize_google(audio) #convert audio to text
                    print('I Heard: {}'.format(data))
                    return data
                except:
                    led.red()
                    return None
            except:
                return None
        
d = Daemon()