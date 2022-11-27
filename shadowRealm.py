#from MotorCode import *

class shadowRealm:

    def __init__(self):
        self.board = self.shadowBoard()

    def banash(self, piece): 
        #shadowRealm.banash(destination, self.getPiece(destination))
        coordinate = self.board.determine_coordinates(piece, True)
        self.board.set(coordinate, piece)
        print(self.board)
        #MotorCode.push_move(origin, coordinate, True)

    def reinstate(self, piece): 
        coordinate = self.board.determine_coordinates(piece, False)
        if coordinate: #if the coordinate even exists, you can get something moved to the board
            self.board.set(coordinate, '.')
        print(self.board)
        #MotorCode.push_move(coordinate, origin, True)
        #shadowRealm.reinstate(destination, promotion_piece)

    #how to reinstate all of the pieces in the correct locations? 
    def reset():
        ...

    class shadowBoard():
        def __init__(self):
            #initialize and make coordinates for each
            self.ROW = [1, 2, 3, 4, 5, 6, 7, 8]
            self.COLUMN = ['x', 'y', 'z']

            #White + Black starts are in the middle 
            self.WHITE_START = 4
            self.WHITE_END = 1
            self.BLACK_START = 5
            self.BLACK_END = 8

            self.white_current = self.COLUMN[0] + str(self.WHITE_START)
            self.black_current = self.COLUMN[0] + str(self.BLACK_START)

            self.SPECIAL_PIECE = ["Q", "R", "q", "r"]

            #create self.data + populate it 
            self.data = []
            self.populate()

        def populate(self):
            for i in range(len(self.ROW)):
                col = []
                for j in range(len(self.COLUMN)):
                    col.append(".")
                self.data.append(col)

        def __repr__(self):
            s = ""
            for i in range(len(self.ROW)):
                for j in range(len(self.COLUMN)):
                    s += self.data[i][j] + " "
                s += "\n"
            return s

        #helper method to get x7 to return the corresponding file + rank in array form
        def array_loc(self, location):  
            file = self.COLUMN.index(location[0])
            rank = len(self.ROW) - int(location[1])
            return (file, rank)

        #helper method: set piece at a location
        def set(self, location, piece): 
            file, rank = self.array_loc(location)
            self.data[rank][file] = piece

        #helper method: get piece from a location 
        def get(self, location):
            file, rank = self.array_loc(location)
            data = self.data[rank][file]
            if data == '.':
                return None #returns none if the space is empty 
            return data

        #get the major piece's location 
        def get_piece_location(self, piece): 
            row = self.BLACK_END 
            if piece.isupper():
                row = self.WHITE_END

            for col in self.COLUMN:
                data = self.get(str(col) + str(row))
                if data == piece:
                    return str(col) + str(row)
            return None

        def determine_coordinates(self, piece, go_in):
            if go_in: #i am going in
                if piece in self.SPECIAL_PIECE: #check if special piece
                    #should be able to change get piece_location for the 
                    # . so it is more versatile
                    #print("The special piece is: ", piece)
                    for char in self.COLUMN:
                        location = char + str(self.BLACK_END)
                        if piece.isupper():
                            location = char + str(self.WHITE_END)
                        current = self.get(location)
                        if current == None:
                            #print("the piece will be stored in: ", location )
                            return location

                if piece.isupper(): #white pieces are uppercase
                    current = self.white_current 
                    if int(current[1]) == self.WHITE_END + 1: 
                        #if the current is at white end of ordered allocation
                        try:
                            self.white_current = self.COLUMN[self.COLUMN.index(current[0]) + 1] + str(self.WHITE_START)
                        except: 
                            print("White is full")
                    else:
                        self.white_current = current[0] + str(int(current[1]) - 1)

                    #print("the piece will be stored in: ", current )
                    #print("the next white piece will be stored in: ", self.white_current)
                    return current
                else:
                    current = self.black_current
                    if int(current[1]) == self.BLACK_END - 1: 
                        try:
                            self.black_current = self.COLUMN[self.COLUMN.index(current[0]) + 1] + str(self.BLACK_START)
                        except:
                            print("Black is full")
                    else:
                        self.black_current = current[0] + str(int(current[1]) + 1)
                    #print("the piece will be stored in: ", current )
                    #print("the next black piece will be stored in: ", self.black_current)
                    return current

            else: 
                #print("where is my queen or major piece?")
                return self.get_piece_location(piece)

'''
s = shadowRealm()
board = s.board
#board.set("x3", "P")

s.banash("Q")
print(board)
s.banash("P")
print(board)
s.banash("p")
print(board)
s.banash("Q")
print(board)
s.banash("r")
print(board)
s.banash("N")
print(board)
s.banash("N")
print(board)
s.banash("B")
print(board)
s.banash("N")
print(board)
s.banash("R")
print(board)
s.reinstate("Q")
print(board)
s.banash("N")
print(board)
s.banash("B")
print(board)
s.banash("N")
print(board)
s.banash("N")
print(board)
s.banash("N")
print(board)
s.banash("B")
print(board)
s.banash("R")
print(board)
s.banash("Q")
print(board)
'''

