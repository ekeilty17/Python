from chessPlayer_AI import *
from random import uniform

def convertBoard(board):
    copy_board = []
    for i in range(0,8):
        copy_board += [list(board[8*i:8*(i+1)])]
    return copy_board

def convert2to1(p):
    #p = [i,j]
    return 8*p[0] + p[1]

def convert1to2(p):
    #p = n
    return [p/8, p%8]

def chessPlayer(board,player):
    new_board = convertBoard(board)
    other_player = 0
    if player == 10:
        other_player = 20
    else:
        other_player = 10
    
    if isCheckMate(new_board,player):
        return [False, [0,0], [ [[0,0], 0], [[0,0], 0], [[0,0], 0] ], None]
    if isCheckMate(new_board,other_player):
        return [False, [0,0], [ [[0,0], 0], [[0,0], 0], [[0,0], 0] ], None]
    
    #Smart AI Code
    board_tree = tree(new_board)
    out = genTree(board_tree,player,3,10)
    if out == False:
        return [False, [0,0], [ [[0,0], 0], [[0,0], 0], [[0,0], 0] ], None]
    Heuristic(board_tree,player)
    
    #getting the move
    out = []
    heuristic_list = []
    for child in board_tree.children:
        heuristic_list += [child.material + child.position]
    if player == 10:
        out = board_tree.children[heuristic_list.index(max(heuristic_list))].move
    elif player == 20:
        out =  board_tree.children[heuristic_list.index(min(heuristic_list))].move
    else:
        out = Random(board,player) 
    if out == []:
        return [False, [0,0], [ [[0,0], 0], [[0,0], 0], [[0,0], 0] ], None]
    move = [convert2to1(out[0]),convert2to1(out[1])]
    
    #getting the cadidate moves, which will be the list of legal moves
    candidate = []
    for i in range(0,64):
        if board[i]/10 == player/10:
            out = GetPieceLegalMoves(new_board, convert1to2(i))
            for m in out:
                candidate += [[[i , convert2to1(m)], round(uniform(0,1),2)]]
    
    #Level order traversal of my tree
    tree_traversal = board_tree.Get_LevelOrder()
    
    return [True, move, candidate, tree_traversal]
