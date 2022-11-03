#from re import S
from phrase import *

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
            command = command.replace(phrase, replacement_dictionary[phrase])

    return command

#stuff = parse(cleanData("queen   x   Bfour promote queen"))
#print(stuff)
