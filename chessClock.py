import time 
import ChessTimer
import concurrent.futures
#import lcd_main as lcd


class ChessClock:
    def __init__(self, timecontrol='10|5'): #(30, 5)  
        slash = timecontrol.index('|')
        self.universalTime = int(timecontrol[:slash])
        self.inc = int(timecontrol[slash + 1:])
        self.timer = ChessTimer.ChessTimer()

        self.whiteTime = self.universalTime * 60 - self.inc      #to convert the seconds to minutes 
        self.blackTime = self.universalTime * 60 - self.inc
        
        #give white and black initializations 
        self.side = True
        self.printing = True

        self.pressClock()
        self.pressClock()

        
    def pressClock(self): #press clock changes the sides each time 
        # the start call press clock to start as white
        if self.side:
            self.increment(True)
            self.timer.switch_to("Black")
        else:
            self.increment(False)
            self.timer.switch_to("White")
        self.switch_turn()

    def switch_turn(self):
        self.side = not self.side
        
    def pause(self):
        self.timer.switch_to("Pause")
        self.switch_turn() #paused so you need to switch back the turn
        self.printing = False

    def resume(self):
        if self.side:
            self.timer.switch_to("White")
        else:
            self.timer.switch_to("Black")
        self.printing = True
        self.tick()

    def increment(self, side):
        if side:
            self.whiteTime += self.inc
        else:
            self.blackTime += self.inc

    def convert(self, seconds): #source: https://www.geeksforgeeks.org/python-program-to-convert-seconds-into-hours-minutes-and-seconds/
        min, sec = divmod(seconds, 60)
        hour, min = divmod(min, 60)
        if sec <= 0 and min <= 0 and hour <= 0:
            return 'Out of Time'
        elif min == 0:
            return seconds
        elif min < 30:
            return '%02d:%02d' % (min, sec)
        else:
            return '%d:%02d:%02d' % (hour, min, sec)

    def restart(self):
        self.timer.all_elapsed_time(self, reset=True)
        self.whiteTime = self.universalTime * 60
        self.blackTime = self.universalTime * 60
        self.side = True
        self.printing = True 

    def __repr__(self):
        timedict = self.timer.all_elapsed_time()

        wtime = round(self.whiteTime - timedict["White"], 2)
        btime = round(self.blackTime - timedict["Black"], 2)
        #print("hhhhhhhhhhhhhwtime: ", wtime)
        #print("btime: ", btime)
        message = ['W:' + str(self.convert(wtime)),'B:' + str(self.convert(btime))]

        print("W:" + str(self.convert(wtime)) + "\n" + "B:" + str(self.convert(btime)))
        return message

    def tick(self):
        while self.printing:
            #lcd.printMessage(self.__repr__())
            print(self.__repr__())
            time.sleep(1)

    def end(self):
        self.printing = False


'''
x = ChessClock('10|3')
x.tick()

x.pressClock()
time.sleep(1)
x.end()
x.pressClock()
time.sleep(2)
x.pause_time()
time.sleep(3)
x.resume_time()
time.sleep(4)
print(x)
'''
