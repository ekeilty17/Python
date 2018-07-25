# Required for LevelOrder Functions
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

    def AddSuccessor(self,T):
        self.children += [T]
        return True

    def DepthFirst(self):
        def rec(node, L=[]):
            L += [node.val]
            for i in range(0,len(node.children)):
                L = rec(node.children[i], L)
            return L
        return rec(self)

    def DepthFirst_style(self):
        def rec(x,indent):
            print indent + str(x.val)
            indent += "\t"
            for i in range(0,len(x.children)):
                rec(x.children[i],indent)
            return True

        return rec(self,"")

    def LevelOrderFlat(self):
        out = []
        q = queue()
        q.enq(self)

        while q.store != []:
            r = q.deq()
            out += [r.val]
            for i in range(0,len(r.children)):
                q.enq(r.children[i])
        return out

    def LevelOrder(self):
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

"""
a = tree(4)
b = tree(10)
c = tree(1)
d = tree(-1)
e = tree(100)
f = tree(-30)

a.AddSuccessor(b)
a.AddSuccessor(c)
a.AddSuccessor(d)

b.AddSuccessor(e)

d.AddSuccessor(f)

print a.DepthFirst()
a.DepthFirst_style()
print a.LevelOrder()
print a.LevelOrderFlat()
print a.InOrder()
