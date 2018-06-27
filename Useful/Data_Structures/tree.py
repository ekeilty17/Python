
class tree:
    def __init__(self,x):
        self.val = x
        self.children = []

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
    
    def InOrder(self):
        def rec(node):
            if node.children == []:
                print node.val
                return None
            print node.val
            for i in range(0,len(node.children)):
                rec(node.children[i])
        rec(self)
