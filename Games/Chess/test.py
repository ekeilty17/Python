#This probably doesn't work, I haven't tested it
#I had it working at one point, but then I changed the way I presented the board up, so I still need to tinker with it

from chessLib import *
import time

def Move(board,pos,new_pos):
    board[new_pos] = board[pos]
    board[pos] = 0

board = genBoard()
printBoard(board)

for i in range(0,100):
    #AI returns a length 2 list
    #comp[0] = piece position
    #comp[1] = piece destination
    t0 = time.time()
    comp = chessPlayer(board,10)
    print "comp",comp[1]
    t1 = time.time()
    print "time",t1-t0
    Move(board,comp[1][0],comp[1][1])
    print printBoard(board)

    #AI returns a length 2 list
    #comp[0] = piece position
    #comp[1] = piece destination
    t0 = time.time()
    print "comp",comp[1]
    comp = chessPlayer(board,20)
    t1 = time.time()
    print "time",t1-t0
    Move(board,comp[1][0],comp[1][1])
    print printBoard(board)
