key_phrase = [ #must be preceeded by "chessbot so chessbot doesn't get confused"
    "resign",
    "start", #i don't think we need this? can we just automatically start
    #once the button is pushed?
    "terminate",
    "pause",
    "resume",
    "reset",
    "play", #this is extracredit to load a pgn and play the game
    "engine" #this is another extracredit to play against an engine 
    ]

replacement_dictionary = { #contain numbers + pieces to be replaced for notation
    "queen": "Q",
    "king": "K",
    "pawn": "", #removes pawn 
    "knight": "N",
    "rook": "R",
    "bishop": "B", #problem with Bishop vs b in Bxd7 or bxe8 
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "promote": "=", #this is the correct way to promote 
    #these two terms shouldn't see any replacements
    "longcastle": "0-0-0",
    "shortcastle": "0-0"
}