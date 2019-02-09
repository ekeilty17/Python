from graph import *

def index_2to1(I, D):
    [i, j] = I
    [n, m] = D

    return i + j*n

def index_1to2(i, D):
    [n, m] = D
    
    return [i%n, i/n]

class grid(graph):

    def __init__(self, n, m=None):
        # n x m = rows x columns
        if m == None:
            m = n 
        
        self.n = n
        self.m = m

        self.grid = []
        for i in range(self.n):
            temp = []
            for j in range(self.m):
                temp += ['.']
            self.grid += [temp]
        
        # init graph
        graph.__init__(self)
        
        # Add verteces
        self.addVertex(n*m)
        
        # Connecting grid lines
        for i in range(n):
            for j in range(m):
                # Including diagonals
                """
                neighbors = [[i-1, j-1], [i, j-1], [i+1, j-1],
                             [i-1, j  ],           [i+1, j  ],
                             [i-1, j+1], [i, j+1], [i+1, j+1]]
                """
                # Not including diagonals
                neighbors = [            [i, j-1],
                             [i-1, j  ],           [i+1, j  ],
                                         [i, j+1]            ]
                neighbors = list(filter(lambda L: L[0] >= 0 and L[0] < self.n and L[1] >= 0 and L[1] < self.m, neighbors))
                neighbors = map(lambda L: L[0] + L[1]*self.n, neighbors)
                for N in neighbors:
                    self.addEdge(i+j*n, N, True, 1)
            
        self.directed = False
    
    def __str__(self):
        out = ""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])-1, -1, -1):
                out += ' ' + self.grid[j][i] + ' '
            out += '\n'
        return out        
    
    def index(self, i, j):
        return self.adj[i + j*self.n]

    def removeNode(self, i, j):
        
        # Removing all edges
        curr = i + j*self.n
        for N in self.getNeighbors(curr):
            self.removeEdge(curr, N)
        
        # updating node list
        self.grid[j][i] = ' '
        
G = grid(10)
print G
G.removeNode(1, 5)
print G
