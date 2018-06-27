class binary_tree:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

    def AddLeft(self,B):
        self.left = B
        return True

    def AddRight(self,B):
        self.right = B
        return True

    def Print_DepthFirst(self):
        def rec(x,indent):
            print indent + str(x.val)
            indent += "\t"
            if x.left != None:
                rec(x.left,indent)
            if x.right != None:
                rec(x.right,indent)
            return True

        return rec(self,"")

    def InOrder(self):
        def rec(node):
            if node == None:
                return None
            rec(node.left)
            print node.val
            rec(node.right)
        rec(self)
