from helper import *

pieces = {  0: 'p',
            1: 'N',
            2: 'B',
            3: 'R',
            4: 'Q',
            5: 'K'
        }

class chess:
    # _ = black square
    # # = white square
    # (makes sense if you are using black as your background in terminal)
    #row a is the 0th row in the list,
    #so the board looks upside down right now
    #like we are playing the game from the black side
    blank_board = [ ['_', '#', '_', '#', '_', '#', '_', '#'],
                    ['#', '_', '#', '_', '#', '_', '#', '_'],
                    ['_', '#', '_', '#', '_', '#', '_', '#'],
                    ['#', '_', '#', '_', '#', '_', '#', '_'],
                    ['_', '#', '_', '#', '_', '#', '_', '#'],
                    ['#', '_', '#', '_', '#', '_', '#', '_'],
                    ['_', '#', '_', '#', '_', '#', '_', '#'],
                    ['#', '_', '#', '_', '#', '_', '#', '_']
                  ]

    def __init__(self):
        self.board = [  [13, 11, 12, 14, 15, 12, 11, 13],
                        [10, 10, 10, 10, 10, 10, 10, 10],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [20, 20, 20, 20, 20, 20, 20, 20],
                        [23, 21, 22, 24, 25, 22, 21, 23]
                     ]
        #TODO use thses variables to account for when both players can castle
        self.canWhiteCastle = True
        self.canBlackCastle = False

    def Display(self):
        out = "\x1b[90m" + "   a  b  c  d  e  f  g  h" + "\x1b[0m" + "\n"
        for i in range(7,-1,-1):
            s_temp =  "\x1b[90m" + str(i+1) + " " + "\x1b[0m"
            for j in range(0,8):
                if self.board[i][j] == 0:
                    if self.blank_board[i][j] == '_':
                        s_temp += " \x1b[30m" + self.blank_board[i][j] + "\x1b[0m "
                    else:
                        s_temp += " \x1b[90m" + self.blank_board[i][j] + "\x1b[0m "
                elif 10 <= self.board[i][j] and self.board[i][j] < 20:
                    s_temp += " \x1b[97m" + pieces[self.board[i][j]-10] + "\x1b[0m "
                elif 20 <= self.board[i][j]:
                    s_temp += " \x1b[34m" + pieces[self.board[i][j]-20] + "\x1b[0m "
            out += s_temp
            if i != 0:
                out += "\n"
        print out
        return out

    def Display_Legal(self,position):
        out = ""
        yellow = GetPieceLegalMoves(self.board, position)
        for i in range(7,-1,-1):
            s_temp = ""
            for j in range(0,8):
                if self.board[i][j] == 0:
                    if [i,j] in yellow:
                        s_temp += " \x1b[33m" + self.blank_board[i][j] + "\x1b[0m "
                    elif self.blank_board[i][j] == '_':
                        s_temp += " \x1b[30m" + self.blank_board[i][j] + "\x1b[0m "
                    else:
                        s_temp += " \x1b[90m" + self.blank_board[i][j] + "\x1b[0m "
                elif 10 <= self.board[i][j] and self.board[i][j] < 20:
                    s_temp += " \x1b[97m" + pieces[self.board[i][j]-10] + "\x1b[0m "
                elif 20 <= self.board[i][j]:
                    s_temp += " \x1b[34m" + pieces[self.board[i][j]-20] + "\x1b[0m "
            out += s_temp
            if i != 0:
                out += "\n"
        print out
        return out

    def gameboard(self):
        out = []
        for row in self.board:
            out += [list(row)]
        return out

    def Move(self,pos,new_pos):
        if self.board[pos[0]][pos[1]] == 0:
            return False
        #get the player
        player = (self.board[pos[0]][pos[1]]/10)*10
        #make the move
        old_pos_val = self.board[new_pos[0]][new_pos[1]]
        self.board[new_pos[0]][new_pos[1]] = self.board[pos[0]][pos[1]]
        self.board[pos[0]][pos[1]] = 0
        #if move causes king to go into check, undo it
        if isInCheck(self.board,player):
            self.board[pos[0]][pos[1]] = self.board[new_pos[0]][new_pos[1]]
            self.board[new_pos[0]][new_pos[1]] = old_pos_val
            return False

        # dealing with castling
        if pos == [0,4] and self.board[new_pos[0]][new_pos[1]] == 15:
            if new_pos == [0,6]:
                self.board[0][5] = 13
                self.board[0][7] = 0
            elif new_pos == [0,2]:
                self.board[0][3] = 13
                self.board[0][0] = 0
        elif pos == [7,4] and self.board[new_pos[0]][new_pos[1]] == 25:
            if new_pos == [7,6]:
                self.board[7][5] = 23
                self.board[7][7] = 0
            elif new_pos == [7,2]:
                self.board[7][3] = 23
                self.board[7][0] = 0

        # dealing with pawn promotion
        # for now I'll just defaul to a queen
        if self.board[new_pos[0]][new_pos[1]] == 10 and new_pos[0] == 7:
            self.board[new_pos[0]][new_pos[1]] = 14
        elif self.board[new_pos[0]][new_pos[1]] == 20 and new_pos[0] == 0:
            self.board[new_pos[0]][new_pos[1]] = 24

        return True
