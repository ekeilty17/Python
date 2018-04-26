def parent(index):
    if index <= 0:
        return False
    if index % 2 == 0:
        return (index-2)/2
    else:
        return (index-1)/2

class heap:

    def __init__(self):
        self.store = []

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
        return True

    def Display(self):
        for i in self.store:
            print i
        return True
    
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

h = heap()
h.add(1)
h.add(20)
h.add(10)
h.add(30)
h.add(100)
h.add(-5)
h.add(20)

h.Display()
print

h.delete_root()
h.Display()
print
h.delete_root()
h.Display()
print
