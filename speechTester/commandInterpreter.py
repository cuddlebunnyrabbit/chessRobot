#from distutils.log import error

replacement_dictionary = { #contain numbers + pieces to be replaced for notation
    "queen": "Q",
    "king": "K",
    "pawn": "", #removes pawn 
    "knight": "N",
    "rook": "R",
    "bishop": "B"
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "promote": "=" #this is the correct way to promote 
}


special_dictionary = { #contain numbers + pieces to be returned immediately
    "longcastle": "0-0-0",
    "shortcastle": "0-0",
    "kingsidecastle": "0-0",
    "queensidecastle": "0-0-0",
    

}

def parse(command):


    if len(command) == 0:
        pass 
        #throw ZeroDivisionError

    # clean the voice_commands
    while " " in command: #remove space
        command = command.replace(' ', '')
    command = command.lower() #lowercase
    command = command.replace('x', '') #remove capture

    for key in 

    for key in pieces_dictionary:
        if key in command:
            command = command.replace(key, pieces_dictionary[key])

    for key in numbers_dictionary:
        if key in command:
            command = command.replace(key, numbers_dictionary[key])

    return command


print("hello")
stuff = parse("Bishop   x   Bfour")
print(stuff)
