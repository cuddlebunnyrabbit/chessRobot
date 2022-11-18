class shadowRealm:

    def __init__(self):
        self.board = self.shadowBoard()
        print(self.board)


    class shadowBoard():
        
        def __init__(self):
            #initialize and make coordinates for each
            self.ROW = [1, 2, 3, 4, 5, 6, 7, 8]
            self.COLUMN = ['x', 'y', 'z']

            self.white_column = 0 #you can be full 0 = x 
            self.white_row = 14
            self.white_major = 0

            #go from x14, x13, x12, then y 14, y13, y12
            self.black_column = 0 #you can be full 
            self.black_row = 14
            self.black_major = 0

            self.data = [['.'] * len(self.COLUMN)] * len(self.ROW)

        def __repr__(self):
            s = ""
            for i in range(len(self.ROW)):
                for j in range(len(self.COLUMN)):
                    s += self.data[i][j] + " "
                s += "\n"
            return s


        def determine_coordinates(self, piece, in_true):
            if in_true: #i am going in 
                if piece.isupper(): #white pieces are uppercase
                    
                else:
                    ...


        def input(self, piece): #expects the coordinates 

        def outtake(self, piece): #expects the coordinates 

        

s = shadowRealm()

