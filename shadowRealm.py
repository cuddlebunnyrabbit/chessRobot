class shadowRealm:

    def __init__(self):
        self.board = self.shadowBoard()
        #print(self.board)

    def determine_coordinates(self, piece, in_true):
            if in_true: #i am going in 
                if piece.isupper(): #white pieces are uppercase
                    ...
                    
                else:
                    ...

    def input(self, piece): #expects the coordinates 
            ...

    def outtake(self, piece): #expects the coordinates 
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
            #location should be column then row x3, y6 for example set by 
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

#print(board.get("x3"))
#print(board)


