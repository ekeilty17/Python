# the point of this file is to confirm that your board data structure
# matches mine. All functions in this code are my own; you may decide
# to refer or use them --- or not.
# 
def getPiece(name):
   if name=="pawn":
      return 0
   elif name=="knight":
      return 1
   elif name=="bishop":
      return 2
   elif name=="rook":
      return 3
   elif name=="queen":
      return 4
   elif name=="king":
      return 5
   else:
      return -1

def genBoard():
   r=[0]*64
   White=10
   Black=20
   for i in [ White, Black ]:
      if i==White:
         factor=+1
         shift=0
      else:
         factor=-1
         shift=63

      r[shift+factor*7] = r[shift+factor*0] = i+getPiece("rook")
      r[shift+factor*6] = r[shift+factor*1] = i+getPiece("knight")
      r[shift+factor*5] = r[shift+factor*2] = i+getPiece("bishop")
      if i==White:
         r[shift+factor*4] = i+getPiece("queen") # queen is on its own color square
         r[shift+factor*3] = i+getPiece("king")
      else:
         r[shift+factor*3] = i+getPiece("queen") # queen is on its own color square
         r[shift+factor*4] = i+getPiece("king")

      for j in range(0,8):
         r[shift+factor*(j+8)] = i+getPiece("pawn")

   return r


pieces = {  0: 'p',
            1: 'N',
            2: 'B',
            3: 'R',
            4: 'Q',
            5: 'K'
        }
def printBoard(board):
   color_board = []
   for i in range(0,64):
       if board[i]/10 == 1:
           color_board += ["  \x1b[97m" + pieces[board[i]%10] + "\x1b[0m  "]
       elif board[i]/10 == 2:
           color_board += ["  \x1b[34m" + pieces[board[i]%10] + "\x1b[0m  "]
       else:
           color_board += ["  \x1b[90m" + "0" + "\x1b[0m  "]
   accum="---- BLACK SIDE ----\n"
   max=63
   for j in range(0,8,1):
      for i in range(max-j*8,max-j*8-8,-1):
         accum=accum+'{0: <10}'.format(color_board[i])
      accum=accum+"\n"
   accum=accum+"---- WHITE SIDE ----"
   return accum

board=genBoard()
print "raw board is: (index=0 ... index=63):"
print board
print "\nwhich will look like the following:"
print printBoard(genBoard())
print ""
print " Note 1: lower right hand square is WHITE"
print " Note 2: two upper rows are for BLACK PIECES"
print " Note 3: two lower rows are for WHITE PIECES"
