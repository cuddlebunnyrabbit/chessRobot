from gpiozero import RGBLED
from time import sleep


class Led:
    def __init__(self):
        #self.color = (1,1,1)
        self.RED = (0,1,1)
        self.BLUE = (1,1,0)
        self.GREEN = (1,0,1)
        self.WHITE = (0,0,0)
        self.CYAN = (1,0,0)
        self.PURPLE = (0,1,0)
        self.OFF = (1,1,1)
        
        self.led = RGBLED(17,18,22,active_high=False)

    def green(self):
        self.color = self.GREEN
        
    def red(self):
        self.led.color = self.RED
    
    def blue(self):
        self.led.color = self.BLUE
        
    def flashing(self):
        for i in range(2):
            self.led.color = self.WHITE
            sleep(1)
            self.led.color = self.CYAN
            sleep(1)
            self.led.color = self.BLUE
            sleep(1)
            self.led.color = self.GREEN
            sleep(1)
            self.led.color = self.PURPLE
            sleep(1)
            self.led.color = self.RED
            sleep(1)
        self.off()
            
    
    def off(self):
        self.led.color = self.OFF
    

'''
led = Led()
led.flashing()

print("I have finished execution")

'''
        

    
    
    
    