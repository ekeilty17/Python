class Queue:
    
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
    
    
    def enq(self, val):
        self.store += [val]

    def deq(self):
        if self.store == []:
            return False
        r = self.store[0]
        self.store = self.store[1:]
        return r
    

if __name__ == "__main__":
    Q = Queue()
    print Q
    Q.enq(10)
    print Q
    Q.enq(20)
    print Q
    Q.enq(30)
    print Q
    Q.enq(40)
    print Q
    print
    Q.deq()
    print Q
    Q.deq()
    print Q
    Q.deq()
    print Q
    Q.deq()
    print Q
