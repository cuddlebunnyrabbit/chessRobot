from MotorCode import *

class shadowRealm:

    def __init__(self):
        self.board = self.shadowBoard()

    def determine_coordinates(self, piece, go_in):
        #going in find your open space
        # 
        '''
        is this a special or a normal piece?
        special:
            go from x to z to see if there is any issues 

        normal:
            remember the previous location 
            move to the next open location 
        ''' 

        #getting out: find your piece 
        #   check from z to x and then see the coordinate that matches 


        if go_in: #i am going in 
            if piece.isupper(): #white pieces are uppercase
                ...
                    
            else:
                ...

    def banash(self, origin, piece): #expects the coordinates 
        #shadowRealm.banash(destination, self.getPiece(destination))
        coordinate = self.determine_coordinates(piece, True)
        MotorCode.push_move(origin, coordinate, True)

    def reinstate(self, origin, piece): #expects the coordinates 
        coordinate = self.determine_coordinates(piece, False)
        MotorCode.push_move(coordinate, origin, True)
        #shadowRealm.reinstate(destination, promotion_piece)

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
            self.data = []

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

        def array_loc(self, location):
            file = self.COLUMN.index(location[0])
            rank = len(self.ROW) - int(location[1])
            return (file, rank)

        def set(self, location, piece): #piece is capitalize or lowercase string 
            file, rank = self.array_loc(location)
            self.data[rank][file] = piece

        def get(self, location):
            file, rank = self.array_loc(location)
            data = self.data[rank][file]
            if data == '.':
                return None #returns none if the space is empty 
            return data

        #you can expand to give some other info 
        def get_piece_location(self, piece): #get the queen's location
            row = self.BLACK_END 
            if piece.isupper():
                row = self.WHITE_END

            for col in self.COLUMN:
                data = self.getter(str(col) + str(row))
                if data != None:
                    if data == piece:
                        return str(col) + str(row)
            return None

s = shadowRealm()
board = s.board
board.set("x3", "P")
print(board)