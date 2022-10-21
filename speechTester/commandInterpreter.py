from phrase import *

def cleanData(command):
    if len(command) == 0:
        return None #throw an error situation when you have no data 
        #is this a good idea? or is this gonna be a silent error?

    while " " in command: #remove space
        command = command.replace(' ', '')
    command = command.lower() #lowercase
    return(command)
    #cannot remove capture! pychess accepts both commands with or without x and it works!
    #wait check your assumptions first 

def parse(command):
    for phrase in key_phrase:
        if phrase == command: #if it is a special phrase 
            pass

    for phrase in special_dictionary:
        pass

    for phrase in replacement_dictionary:
        if phrase in command:
            command = command.replace(phrase, replacement_dictionary[phrase])

    return command

stuff = parse(cleanData("Bishop   x   Bfour"))
print(stuff)
