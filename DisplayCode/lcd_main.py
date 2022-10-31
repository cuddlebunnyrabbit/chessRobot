"""Implements user input to display on lcd"""

from lcd_api import LcdApi
from i2c_lcd import I2cLcd

I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

lcd = I2cLcd(1, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

def printMessage(messageList):
    lcd.putstr(messageList[0])
    lcd.move_to(0, 1)
    lcd.putstr(messageList[1])