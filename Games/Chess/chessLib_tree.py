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

class tree:
    def __init__(self,x):
        self.val = x
        self.move = []
        self.children = []
        self.material = 0
        self.position = 0

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

    def Get_LevelOrder(self):    
        out = []
        q = queue()
        q.enq(self)

        while q.store != []:
            r = q.deq()
            out += [r]
            for i in range(0,len(r.children)):
                q.enq(r.children[i])
        return out
