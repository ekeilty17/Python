from board import *
from tree import *

""" Finding any Knight's Tour """

def search(root):
    root.val.Display()
    if root.val.isComplete():
        return root
    
    # If there exists a square with 0 possible knight moves,
    #   then it's impossible to ever get to that sqare, 
    #   thus that board state could never be a knights tour
    # If there exists two squares each with 1 possible knight move,
    #   then that board state can't be a knights tour either bc you could get to each square
    #   but after that you wouldn't be able to get out of it
    cnt = 0
    for i in range(root.val.rows):
        for j in range(root.val.cols):
            if root.val.visited[i][j] == 0:
                if root.val.Num_Knight_Moves([i,j]) == 0:
                    return False
                elif root.val.Num_Knight_Moves([i,j]) == 1:
                    cnt += 1
                    if cnt == 2:
                        return False
    
    # I will implement Warnsdorf's rule, 
    #   which is a heuristic when finding knights tours
    #   which says to pick the square with the least number of moves
    possible = root.val.Possible_Knight_Moves()
    possible = sorted(possible, key=root.val.Num_Knight_Moves)
    
    # Using a Depth-First Search
    for i in range(len(possible)):
        #initializing child
        child = root.val.new()
        child.Move(possible[i])
        root.AddSuccessor(tree(child))
        #searching
        r = search(root.children[-1])
        if r != False:
            return r
    return False

def back_track(leaf, L=[]):
    if leaf == None:
        return L
    #if leaf.parent == None:
    #    return [leaf.val] + L
    return back_track(leaf.parent, [leaf.val] + L)

#Change to taking a class as an input?
def Knights_Tour(B):
    
    leaf = search(tree(B))
    if leaf == False:
        print "Knight's tour is not possible from this square"
        return []
    return back_track(leaf)



""" Finding a Closed Knight's Tour """

def search_closed(root):
    root.val.Display()
    if root.val.isClosed():
        return root
   
    # If there are no knight moves that can get to back to the start
    # then it can't be a closed knights tour
    if root.val.Num_Knight_Moves(root.val.start) == 0:
        return False

    # Getting rid of impossible cases
    cnt = 0
    for i in range(root.val.rows):
        for j in range(root.val.cols):
            if root.val.visited[i][j] == 0:
                if root.val.Num_Knight_Moves([i,j]) == 0:
                    return False
                elif root.val.Num_Knight_Moves([i,j]) == 1:
                    cnt += 1
                    if cnt == 2:
                        return False
    
    
    
    # Warnsdorf's rule 
    possible = root.val.Possible_Knight_Moves()
    possible = sorted(possible, key=root.val.Num_Knight_Moves)
    
    # Using a Depth-First Search
    for i in range(len(possible)):
        #initializing child
        child = root.val.new()
        child.Move(possible[i])
        root.AddSuccessor(tree(child))
        #searching
        r = search_closed(root.children[-1])
        if r != False:
            return r
    return False

#back_track function works the same

def Closed_Knights_Tour(B):
    
    #Use some mathematical theorems so I don't fall into an infinite search
    if B.rows%2 == 1 and B.cols%2 == 1:
        print "A complete Knight's Tour is impossible with these dimensions."
        return False
    elif min(B.rows,B.cols) in [1,2,4]:
        print "A complete Knight's Tour is impossible with these dimensions."
        return False
    elif min(B.rows,B.cols) == 3 and max(B.rows,B.cols) in [4,6,8]:
        print "A complete Knight's Tour is impossible with these dimensions."
        return False
    
    leaf = search_closed(tree(B))
    if leaf == False:
        print "Knight's tour is not possible from this square"
        return []
    return back_track(leaf)
