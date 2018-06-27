class conway:
    row_num = 0
    col_num = 0
    what = ''
    store = []

    def __init__(self,init_row_num,init_col_num,init_what):
        self.row_num = init_row_num
        self.col_num = init_col_num
        self.what = init_what
        
        if (self.what == 'zeros'):
            for i in range(0,self.row_num):
                temp = []
                for j in range(0,self.col_num):
                    temp += [0]
                self.store += [temp]
        elif (self.what == 'random'):
            from random import randint
            for i in range(0,self.row_num):
                temp = []
                for j in range(0,self.col_num):
                    temp += [randint(0,1)]
                self.store += [temp]

    def getDisp(self):
        board = ""
        for e in self.store:
            for i in range(0,len(e)):
                if (e[i] == 0):
                    board += " "
                elif (e[i] == 1):
                    board += "*"
                else:
                    return False
            board += "\n"
        return board
    
    def printDisp(self):
        if (self.getDisp() == False):
            return False
        else:
            print self.getDisp()
            return True

    def printDisp2(self):
        board = "  "
        for i in range(0,len(self.store[0])):
            board += str(i)
        board += "\n"
        counter = 0
        for e in self.store:
            board += str(counter) + " "
            for i in range(0,len(e)):
                if (e[i] == 0):
                    board += "0"
                elif (e[i] == 1):
                    board += "1"
                else:
                    return False
            board += "\n"
            counter += 1
        print board

    def setPos(self,row,col,val):
        if ((val != 0) and (val != 1)):
            return False
        if ((row >= self.row_num) or (col >= self.col_num)):
            return False
        self.store[row][col] = val
        return True

    def getNeighbours(self,row,col):
        
        if( (row > (self.row_num-1)) or (col > (self.col_num-1)) or
             (row < 0) or (col < 0) ):
            #out of range
            return False
        else:
            neighbours = []
            neighbour_coord = [ [row-1,col-1], [row-1,col], [row-1,col+1], 
                                [row,  col-1],              [row,  col+1], 
                                [row+1,col-1], [row+1,col], [row+1,col+1] 
                                ]
            for e in neighbour_coord: 
                    neighbours += [ self.store[ e[0]%self.row_num ][ e[1]%self.col_num ] ]
            
            return neighbours

    def evolve(self, rule):
        next_state = []
        for i in range(0,self.row_num):
            temp = []
            for j in range(0,self.col_num):
                temp += [rule(self.store[i][j], self.getNeighbours(i,j))]
            next_state += [temp]
        self.store = next_state
