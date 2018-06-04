class stack:
    store = []

    def push(self,val):
        self.store += [val]

    def pop(self):
        if self.store == []:
            return False
        r = self.store[0]
        self.store = self.store[0:len(self.store)-1]
        return r
    
    def Displ(self):
        for i in range(0,len(self.store)):
            print self.store[i]

x = stack()
x.push(10)
x.push(20)
x.push(30)
x.push(40)
x.Displ()
print
x.pop()
x.Displ()
print
x.pop()
x.Displ()
print
x.pop()
x.Displ()
print
x.pop()
x.Displ()
print
x.pop()
x.Displ()
print
x.pop()
x.Displ()
