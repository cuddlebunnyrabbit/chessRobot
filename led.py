from gpiozero import RGBLED
from time import sleep

led = RGBLED(17,18,22,active_high=False)

valid_move = (1,0,1)
invalid_move = (0,1,1)
listen = (1,1,0)


move = input("valid or invalid")

while True:
    if move == "valid":
        led.color = valid_move
        sleep(10)
        move = input("valid or invalid")
    elif move == "invalid":
        led.color = invalid_move
        sleep(10)
        move = input("valid or invalid")
    elif move == "listen":
        led.color = listen
        sleep(10)
        move = input("valid or invalid")
        
    
    
    
    