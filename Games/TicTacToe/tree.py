class queue:
    
    def __init__(self):
        self.store = []

    def enq(self, val):
        self.store += [val]

    def deq(self):
        if self.store == []:
            return False
        r = self.store[0]
        self.store = self.store[1:len(self.store)]
        return r

    def Displ(self):
        for i in range(0,len(self.store)):
            print self.store[i]

class tree:
    def __init__(self,x):
        self.val = x
        self.children = []
        self.heuristic = 0

    def AddSuccessor(self,T):
        self.children += [T]
        return True

    def Print_DepthFirst(self):
        def rec(x,indent):
            print indent + str(x.val)
            indent += "\t"
            for i in range(0,len(x.children)):
                rec(x.children[i],indent)
            return True

        return rec(self,"")
    
    def InOrder(self):
        def rec(node):
            if node.children == []:
                print node.val
                return None
            print node.val
            for i in range(0,len(node.children)):
                rec(node.children[i])
        rec(self)


    def Get_LevelOrder(self):
        out = []
        q = queue()
        q.enq(self)
        
        while q.store != []:
            r = q.deq()
            out += [r.val]
            for i in range(0,len(r.children)):
                q.enq(r.children[i])
        return out
    
    def Get_LevelOrder2(self):
        out = []
        q = queue()
        q.enq(self)

        while q.store != []:
            count = len(q.store)
            temp = []
            while count > 0:
                r = q.deq()
                temp += [r.val]
                for i in range(0,len(r.children)):
                    q.enq(r.children[i])
                count -= 1;
            out += [temp]
        return out
