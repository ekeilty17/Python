class Stack:

    def __init__(self, store=[]):
        self.store = store

    def __str__(self):
        return str(self.store)
        
    def __getitem__(self, i):
        return self.store[i]

    def __len__(self):
        return len(self.store)

    def isEmpty(self):
        return len(self) == 0
    
    def push(self,val):
        self.store += [val]

    def pop(self):
        if self.isEmpty():
            return False
        r = self.store[0]
        self.store = self.store[:-1]
        return r
    

if __name__ == "__main__":
    S = Stack()
    print S
    S.push(10)
    print S
    S.push(20)
    print S
    S.push(30)
    print S
    S.push(40)
    print S
    print
    S.pop()
    print S
    S.pop()
    print S
    S.pop()
    print S
    S.pop()
    print S
    S.pop()
    print S
    S.pop()
    print S
