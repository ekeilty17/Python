class tree:
    def __init__(self,x):
        self.val = x
        self.children = []
        self.parent = None
        
    def AddSuccessor(self,T):
        self.children += [T]
        T.parent = self
        return True
