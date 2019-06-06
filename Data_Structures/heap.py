def parent(index):
    if index <= 0:
        return False
    if index % 2 == 0:
        return (index-2)/2
    else:
        return (index-1)/2

class Heap:

    def __init__(self):
        self.store = []

    def __str__(self):
        return str(self.store)
    
    def __len__(self):
        return len(self.store)
    
    def __getitem__(self, i):
        return self.store[i]
    
    def getParent(self, i):
        if i <= 0:
            return None
        if i % 2 == 0:
            return (i-2)/2
        else:
            return (i-1)/2

    def add(self, val):
        self.store += [val]
        #bubble up
        index = len(self.store) - 1
        while True:
            if index == 0:
                break
            if self.store[index] < self.store[parent(index)]:
                break
            #swap
            temp = self.store[index]
            self.store[index] = self.store[parent(index)]
            self.store[parent(index)] = temp
            index = parent(index)
    
    def delete_root(self):
        #swap root with last element
        temp = self.store[0]
        self.store[0] = self.store[len(self.store)-1]
        self.store[len(self.store)-1] = temp
        #remove last element
        self.store = self.store[0:len(self.store)-1]
        #bubble down element in root to maintain heap structure
        index = 0
        while True:
            if 2*index+1 >= len(self.store):
                break

            if 2*index+1 < len(self.store) and 2*index+2 >= len(self.store):
                if self.store[index] < self.store[2*index+1]:
                    temp = self.store[index]
                    self.store[index] = self.store[2*index+1]
                    self.store[2*index+1] = temp
                    index = 2*index+1
                break

            if self.store[index] > self.store[2*index+1] and self.store[index] > self.store[2*index+2]:
                break
            
            if self.store[2*index+1] > self.store[2*index+2]:
                temp = self.store[index]
                self.store[index] = self.store[2*index+1]
                self.store[2*index+1] = temp
                index = 2*index+1
            else:
                temp = self.store[index]
                self.store[index] = self.store[2*index+2]
                self.store[2*index+2] = temp
                index = 2*index+2

if __name__ == "__main__":
    H = Heap()
    H.add(1)
    H.add(20)
    H.add(10)
    H.add(30)
    H.add(100)
    H.add(-5)
    H.add(20)

    print H
    print

    H.delete_root()
    print H
    print
    H.delete_root()
    print H
    print
