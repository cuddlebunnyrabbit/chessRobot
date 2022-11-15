#from re import S
from phrase import *
from chess import *

def cleanData(command):
    '''
    if len(command) == 0:
        return None #throw an error situation when you have no data 
        #is this a good idea? or is this gonna be a silent error?
'''
    while " " in command: #remove space
        command = command.replace(' ', '')
    command = command.lower() #lowercase
    return(command)
  
def parse(command):
    for word in key_phrase:
        if word in command:
            return word

    for word in replacement_dictionary:
        if word in command: #clean up the command into a phrase  
            command = command.replace(word, replacement_dictionary[word])

    '''
    print("This is command 1/2 way in the parser: ", command)

    print(SQUARE_NAMES)
    print(command[:2])
    print(command[2:])
    '''

    #checks if the command is an actual valid move 
    if len(command) != 4:
        return None
    
    elif command[:2] in SQUARE_NAMES and command[2:] in SQUARE_NAMES:
        return command

    return None

#stuff = parse(cleanData("queen   x   Bfour promote queen"))
#print(stuff)
