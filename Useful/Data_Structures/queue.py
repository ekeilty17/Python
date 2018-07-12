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

x = queue()
x.enq(10)
x.enq(20)
x.enq(30)
x.enq(40)
x.Displ()
print
x.deq()
x.Displ()
print
x.deq()
x.Displ()
print
x.deq()
x.Displ()
print
x.deq()
x.Displ()
