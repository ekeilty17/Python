class Queue:
    def __init__(self):
        self.store = []
    
    def isEmpty(self):
        return len(self.store) == 0

    #had to rename the queue functions
    def push(self, val):
        self.store += [val]

    #so that it works generally
    def pop(self):
        if self.isEmpty():
            return None
        r = self.store[0]
        self.store = self.store[1:]
        return r


class Stack:
    def __init__(self):
        self.store = []
    
    def isEmpty(self):
        return len(self.store) == 0

    def push(self,val):
        self.store += [val]

    def pop(self):
        if self.isEmpty():
            return None
        r = self.store[-1]
        self.store = self.store[:-1]
        return r

class Graph(object):
    def __init__(self):
        self.adj = []
        self.directed = False
        # self.adj will have the form [ [[node, weight], [node, weight], ...], 
        #                               [[node, weight], [node, weight], ...], ... ]
    
    def __getitem__(self, v):
        return self.adj[v]
    
    def __len__(self):
        return len(self.adj)

    def addVertex(self, N=1):
        if N > 0:
            for v in range(N):
                self.adj += [[]]
        return len(self.adj)

    def addEdge(self, from_idx, to_idx, directed=False, weight=1):
        # error checks
        if from_idx < 0 or from_idx >= len(self.adj):
            raise TypeError("Starting node does not exit in the graph.")
        if to_idx < 0 or to_idx >= len(self.adj):
            raise TypeError("Ending node does not exist in the graph.")
        if directed != True and directed != False:
            raise TypeError("variable 'directed' must be a boolean.")
        if weight == 0:
            # A weight of zero implies no connection
            return None

        # I could check if [to_idx,weight] in  self.adj[from_idx]
        # Allow this means this is technically a multigraph, but I will allow it
        # in order to maintain as much generality as possible
        
        self.adj[from_idx] += [(to_idx, weight)]
        if not directed:
            self.adj[to_idx] += [(from_idx, weight)]
        else:
            self.directed = True

    def __str__(self):
        out = ""
        for v in range(len(self.adj)):
            out += "Node " + str(v) + ":\t"
            if v < 10:
                out += '\t'
            for node, weight in self.adj[v]:
                out += '{(' + str(node) + '), ' + str(weight) + '}'
                # This technically won't print correctly if the adjacency list contains a duplicate element
                if (node, weight) != self.adj[v][-1]:
                    out += ', '
            out += '\n'
        return out

    def getWeight(self, from_idx, to_idx):
        neighbor_idx = None
        try:
            neighbor_idx = [node for node, _ in self.adj[from_idx]].index(to_idx)
            return self.adj[from_idx][neighbor_idx][1]
        except:
            return 0
    
    def getNeighbors(self, v):
        return [node for node, _ in self.adj[v]]
    
    # From now on I will use A and B for the starting and ending node respectively
    # It is just shorter than the more descriptive from_idx and to_idx notation
    def removeEdge(self, A, B):
        self.removeSingleEdge(A, B)
        if not self.directed:
            self.removeSingleEdge(B, A)
    
    def removeSingleEdge(self, A, B):
        # Error Checking
        if A < 0 or A >= len(self.adj):
            raise TypeError("Starting node does not exit in the graph.")
        if B < 0 or B >= len(self.adj):
            raise TypeError("Ending node does not exist in the graph.")
        
        # This will remove all duplicate edges
        self.adj[A] = list(filter(lambda x: x[0] != B, self.adj[A]))
        
    def AdjMatrix(self):
        out = []
        for i in range(len(self.adj)):
            temp = [0] * len(self.adj)
            for node, weight in self.adj[i]:
                temp[node] = weight
            out += [temp]
        return out

    def printAdjMatrix(self):
        M = self.AdjMatrix()
        for r in M:
            print r
    

    # Some functions to tell you infromation about the graph
    
    # This is how you could write it to figure it out computationally
    # but I just stored it as a variable
    """
    def isDirected(self):
        for i in range(0,len(self.adj)):
            for j in range(0,len(self.adj[i])):
                if i not in self.getNeightbors(self.getNode(i, j)):
                    return True
        return False
    """
    def isDirected(self):
        return self.directed

    def Degree(self, v):
        if v < 0 or v >= len(self.adj):
            raise TypeError("That node does not exist in the graph.")
        if self.isDirected():
            raise TypeError("The graph is directed, trying calling the methods outDegree() or inDegree().")
        return len(self.adj[v])

    def outDegree(self, v):
        if v < 0 or v >= len(self.adj):
            raise TypeError("That node does not exist in the graph.")
        return len(self.adj[v])

    def inDegree(self, v):
        if v < 0 or v >= len(self.adj):
            raise TypeError("That node does not exist in the graph.")
        count = 0
        for i in range(len(self.adj)):
            for node, _ in self.adj[i]:
                if node == v:
                    count += 1
        return count

    # Some functions that do useful things to the graph

    def Dijkstra(self, start, end):
         # Initialize all dists as infinite
        dist = [-1] * len(self)
        # Initialize all paths as undefined
        path = [[]] * len(self)
        # Create a vertex set initialized with all verteces
        Q = range(len(self))
        # This is technically not necessary, but significantly speeds things up
        visited = [False] * len(self)

        # First distance is given
        dist[start] = 0
        path[start] = []

        while len(Q) != 0:

            #print len(Q)

            # Find vertex with min distance to previous node and remove it
            u = -1
            min_dist = -1
            for n in range(len(self)):
                if dist[n] == -1 or visited[n]:
                    continue
                if u == -1 or dist[n] < min_dist:
                    u = n
                    min_dist = dist[n]
            #print Q, dist, visited, u
            if u == -1:
                Q = []
                continue
            Q.remove(u)
            visited[u] = True

            Neighbors = self.getNeighbors(u)
            Neighbors = list(filter(lambda x: x in Q, Neighbors))
            Neighbors = list(sorted(Neighbors, key=lambda x: self.getWeight(u, x)))

            for v in Neighbors:
                if not visited[v]:
                    # if current path shorter than previous path (remember -1 = inf)
                    if ( dist[v] == -1 ) or ( dist[u] + self.getWeight(u, v) < dist[v]) :
                        dist[v] = dist[u] + self.getWeight(u, v)
                        path[v] = path[u] + [u]

        return (dist[end], path[end] + [end])

    def traverse(self, start=None, searchType='depth'):
        if start > len(self):
            raise TypeError("Node does not exist in the graph")
        if start != None:
            if start < 0:
                return []
        if searchType != 'depth' and searchType != 'breadth':
            return []
        
        # initializing the queue/stack
        C = None
        if searchType == 'depth':
            C = Queue()
        else:
            C = Stack()

        # helper lists to keep track of where I've been
        visited = [False] * len(self)
        processed = [False] * len(self)

        # dealing with the weird starting case
        V = self.adj
        n = len(self) if start == None else 1

        out = []
        for i in range(n):
            temp = []
            # this is also to deal with the weird start case
            if start == None:
                if visited[i] == False:
                    C.push(i)
                    visited[i] = True
            else:
                if visited[start] == False:
                    C.push(start)
                    visited[start] = True
            # actual algorithm
            while not C.isEmpty():
                w = C.pop()
                if processed[w] == False:
                    temp += [w]
                    processed[w] = True
                for node, _ in V[w]:
                    if visited[node] == False:
                        C.push(node)
                        visited[node] = True
            if temp != []:
                out += [temp]
        return out

if __name__ == "__main__":
    G = Graph()
    G.addVertex(5)
    G.addEdge(0,1,True,1)
    G.addEdge(0,2,True,1)
    G.addEdge(0,3,True,1)
    G.addEdge(0,4,True,1)
    G.addEdge(1,3,True,1)
    G.addEdge(2,1,True,1)
    G.addEdge(2,4,True,2)
    G.addEdge(3,4,True,1)
    G.addEdge(3,2,True,1)
    G.addEdge(3,2,True,1)
    print "Represenation of the Graph"
    print G
    print G[0]
    print
    print G.traverse(searchType='breadth')
    print
    #print "Remove Edge"
    #G.removeEdge(1,3)
    #G.removeEdge(2,4)
    #G.removeEdge(0,0)
    #print G
    print
    G.printAdjMatrix()
