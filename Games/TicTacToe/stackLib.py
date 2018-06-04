class stack:
    store = []
    
    def __init__(self):
        self.store = []
    
    def push(self, val):
        self.store += [val]

    def pop(self):
        if self.store == []:
            return False
        p = self.store[len(self.store)-1]
        self.store = self.store[0:len(self.store)-1]
        return p
