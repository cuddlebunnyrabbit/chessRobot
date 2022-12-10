import time 
from threading import Timer

class ChessClock:
    class RepeatTimer(Timer):
        def run(self):
            while not self.finished.wait(self.interval):
                self.function(*self.args,**self.kwargs)
            print('Done')

        def display(msg):
            print(msg + ' ' + time.strftime('%H:%:M:%S'))

    def __init__(self, timecontrol = '10|5'): #(30, 5)
        
        slash = timecontrol.index('|')
        self.total = int(timecontrol[:slash])
        self.inc = int(timecontrol[slash + 1: ])
        self.current = self.total
        timer = self.RepeatTimer(1,self.RepeatTimer.display,['Repeating'])
        
        timer.start()
        print('threading started')
        time.sleep(self.remain)
        print('threading finishing')
        timer.cancel()
        

    def increment(self):
        self.remain += self.inc
        time.sleep(self.inc)
    
x = ChessTimer('5|10')

x.increment()

    #things you can do: 
    # 1. choose time control using voice 
    # 2. choose increment or delay? how to do? 
    # 3. 2 modes for display. if very close then make sure to display code closer 
    #https://www.youtube.com/watch?v=Mp6YMt8MSAU&ab_channel=ComputerScienceTutorials