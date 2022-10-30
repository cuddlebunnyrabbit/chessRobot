from re import S
from phrase import *

def cleanData(command):
    if len(command) == 0:
        return None #throw an error situation when you have no data 
        #is this a good idea? or is this gonna be a silent error?

    while " " in command: #remove space
        command = command.replace(' ', '')
    command = command.lower() #lowercase
    return(command)
  
def parse(command):
    for phrase in key_phrase:
        if phrase == command: #if it is a special phrase that would trigger 
            #some mode change in chessBot. if they will resign game or something
            
            #pass the command into the problem
            #return stop gameOn or something?
            pass

    for phrase in replacement_dictionary:
        if phrase in command: #clean up the command into a phrase  
            command = command.replace(phrase, replacement_dictionary[phrase])

    return command

stuff = parse(cleanData("queen   x   Bfour promote queen"))
print(stuff)
