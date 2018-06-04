#This AI needs work
#I wrote this when I was trying to figure out how to use trees to do a brute force calculation
#I didn't do an amazing job...could use some cleaning up

from random import randint
from stackLib import *
from tree import *

def AnalyzeBoard(T):
    #return list
    #-1: Error
    #0: incomplete game
    #1: X wins
    #2: O wins
    #3: draw

    for i in T:
        if (type(i) != int or i < 0 or i > 2):
            return -1

    #unfortunately this is specific to a 3x3
    #bc I couldn't be bottered to find a general way
    for i in range(0,3):
        #rows
        if (T[0+i*3] == T[1+i*3] == T[2+i*3] == 1):
            return 1
        if (T[0+i*3] == T[1+i*3] == T[2+i*3] == 2):
            return 2
        
        #collumns
        if (T[0+i] == T[3+i] == T[6+i] == 1):
            return 1
        if (T[0+i] == T[3+i] == T[6+i] == 2):
            return 2
    
    #diagonals
    if (T[0] == T[4] == T[8] == 1):
        return 1
    if (T[0] == T[4] == T[8] == 2):
        return 2
    if (T[2] == T[4] == T[6] == 1):
        return 1
    if (T[2] == T[4] == T[6] == 2):
        return 2

    for i in T:
        if i == 0:
            return 0

    return 3

def Random(board,player):
    possible_moves = []
    for i in range(0,len(board)):
        if board[i] == 0:
            possible_moves += [i]
    return possible_moves[randint(0,len(possible_moves)-1)]

def genWinningMove(board,player):
    for i in range(0,3):
        #rows                           
        if ((board[0+3*i] == board[1+3*i] == player) and (board[2+3*i] == 0)):
            return 2+3*i
        elif ((board[1+3*i] == board[2+3*i] == player) and (board[0+3*i] == 0)):
            return 0+3*i
        elif ((board[0+3*i] == board[2+3*i] == player) and (board[1+3*i] == 0)):
            return 1+3*i
        #columns
        if ((board[0+i] == board[3+i] == player) and (board[6+i] == 0)):
            return 6+i
        elif ((board[3+i] == board[6+i] == player) and (board[0+i] == 0)):
            return 0+i
        elif ((board[0+i] == board[6+i] == player) and (board[3+i] == 0)):
            return 3+i

    #diagonal 1
    if ((board[0] == board[4] == player) and (board[8] == 0)):
        return 8
    elif ((board[4] == board[8] == player) and (board[0] == 0)):
        return 0
    elif ((board[0] == board[8] == player) and (board[4] == 0)):
        return 4

    #diagonal 2
    if ((board[2] == board[4] == player)) and (board[6] == 0):
        return 6
    elif ((board[4] == board[6] == player) and (board[2] == 0)):
        return 2
    elif ((board[2] == board[6] == player) and (board[4] == 0)):
        return 4

    return -1

def genNonLoser(board,player):
    if (player == 1):
        return genWinningMove(board,2)
    elif (player == 2):
        return genWinningMove(board,1)
    else:
        return -1

def blind(board, player):
    if genWinningMove(board,player) != -1:
        return genWinningMove(board,player)
    if genNonLoser(board,player) != -1:
        return genNonLoser(board,player)
    return Random(board,player)

def Heuristic(board, player):
    other_player = 0
    if player == 1:
        other_player = 2
    if player == 2:
        other_player == 1
    
    if AnalyzeBoard(board) == player:
        return 1
    elif AnalyzeBoard(board) == other_player:
        return -1
    elif AnalyzeBoard(board) == 3:
        return 0
    elif genWinningMove(board,player) != -1:
        return 1
    elif genNonLoser(board,player) != -1:
        return -1
    else:
        return 0
"""
def make_move(board, player, move):
    temp = list(board)
    temp[move] = player
    return temp

def unmake_move(board, player, move):
    temp = list(board)
    temp[move] = 0
    return temp
"""
def onelook(board,player):
    if genWinningMove(board,player) != -1:
        return genWinningMove(board,player)
    if genNonLoser(board,player) != -1:
        return genNonLoser(board,player)
    
    moves = []
    for i in range(0,len(board)):
        if board[i] == 0:
            moves += [i]
    
    next_boards = []
    for i in range(0, len(moves)):
        temp = list(board)
        temp[moves[i]] = player
        next_boards += [temp]

    for i in range(0, len(next_boards)):
        if Heuristic(next_boards[i], player) == 1:
            return moves[i]

    return Random(board,player)

#adds every possible move until the end of the game
def add_moves(board_node,player):
    #getting empty spots
    indexes = []
    for i in range(0,len(board_node.val)):
        if board_node.val[i] == 0:
            indexes += [i]
    #base case for the recussion,
    #if there are no more spots then the tree is done
    if indexes == []:
        return False
    
    #add moves to children
    for i in indexes:
        A = list(board_node.val)
        A[i] = player
        x = tree(A)
        board_node.AddSuccessor(x)
    
    other_player = 0
    if player == 1:
        other_player = 2
    if player == 2:
        other_player = 1
    
    #call function on children
    for i in range(0,len(board_node.children)):
        add_moves(board_node.children[i], other_player)
    return True

#assumes the opponent wont make stupid moves in order to limit
#some of the possibilities
def add_moves_smart(board_node,player):
    #getting empty spots
    indexes = []
    for i in range(0,len(board_node.val)):
        if board_node.val[i] == 0:
            indexes += [i]
    #base case for the recussion,
    #if there are no more spots then the tree is done
    if indexes == []:
        return False
    
    #if we can win, go there
    if genWinningMove(board_node.val,player) != -1:
        A = list(board_node.val)
        A[genWinningMove(board_node.val,player)] = player
        x = tree(A)
        board_node.AddSuccessor(x)
        return True #break since we won
    #to block the opponent from winning
    elif genNonLoser(board_node.val,player) != -1:
        A = list(board_node.val)
        A[genNonLoser(board_node.val,player)] = player
        x = tree(A)
        board_node.AddSuccessor(x)
    else:
        #add moves to children
        for i in indexes:
            A = list(board_node.val)
            A[i] = player
            x = tree(A)
            board_node.AddSuccessor(x)
    
    other_player = 0
    if player == 1:
        other_player = 2
    if player == 2:
        other_player = 1
    
    #call function on children
    for i in range(0,len(board_node.children)):
        add_moves_smart(board_node.children[i], other_player)
    return True

def searchTree(root, val):
    if root.val == None:
        return False
    if root.val == val:
        return True
    else:
        found = False
        curr = root.children
        for i in range(0,len(root.children)):
            if found:
                break
            found = searchTree(root.children[i], val)
        return found

def genHeuristics(root, player):
    if root.val == None:
        return False

    other_player = 0
    if player == 1:
        other_player = 2
    if player == 2:
        other_player = 1

    #base case
    if root.children == []:
        an = AnalyzeBoard(root.val)
        if an == player:
            root.heuristic = 1
        elif an == other_player:
            root.heuristic = -1
        elif genWinningMove(root.val,player) != -1:
            root.heuristic = -1
        elif genNonLoser(root.val,player) != -1:
            root.heuristic = 1
        return True
    
    #calling the function on all the children
    for i in range(0,len(root.children)):
        genHeuristics(root.children[i], player)
    
    #now that the children have been assigned a heuristic, we can sum it
    #averaging the Heuristic of the children to get Heuristic of the parent
    avg = 0.0
    for i in range(0,len(root.children)):
        avg += root.children[i].heuristic
    root.heuristic = avg/len(root.children)
    print root.val, root.heuristic
    return True

def setHeuristicsZero(root):
    if root.val == None:
        return False
    if root.children == []:
        root.heuristic = 0
    for i in range(0,len(root.children)):
        setHeuristicsZero(root.children[i])
    return True

def brute_force(board, player):
    if genWinningMove(board,player) != -1:
        return genWinningMove(board,player)
    if genNonLoser(board,player) != -1:
        return genNonLoser(board,player)
    
    board_tree = tree(board)

    #count the zeros on the board
    zeros = 0
    for i in board:
        if i == 0:
            zeros += 1
    if zeros > 5:
        add_moves_smart(board_tree,player)
    else:
        add_moves(board_tree,player)

    board_tree.Print_DepthFirst()
    genHeuristics(board_tree,player)
    
    #finding the max heuristic
    max_h = -10 #max should never be more or less than +/- 1
    max_h_index = -1
    for i in range(0,len(board_tree.children)):
        if board_tree.children[i].heuristic > max_h:
            max_h_index = i
            max_h = board_tree.children[i].heuristic
    
    #resetting heuristics
    setHeuristicsZero(board_tree)

    #finding the move of the child with the best heuristic
    move = -1
    for i in range(0,9):
        if board_tree.val[i] != board_tree.children[max_h_index].val[i]:
            move = i
    
    return move
