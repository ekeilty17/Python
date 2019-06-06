from binary_tree import binary_tree

class AVL_tree(binary_tree):
    
    def __init__(self, val):
        BinaryTree.__init__(self, val)
        self.height = self.assign_heights()
    
    def assign_heights(self):
        if self == None:
            return -1
        L = -1
        R = -1
        if self.left != None:
            L = self.left.assign_heights()
        if self.right != None:
            R = self.right.assign_heights()
        
        self.height = max(L, R) + 1
        return self.height
    
    def balance_factor(self):
        if self == None:
            return 0

        bf = 0
        if self.left != None:
            bf -= self.left.height+1
        if self.right != None:
            bf += self.right.height+1
        
        return bf
    
    def rotate_right(self):
        if self == None:
            return False
        if self.left == None:
            return False
        
        # Rotating
        t1 = self.left
        t2 = t1.right
        t1.right = self
        self.left = t2
        
        t1.assign_heights()
        return t1

    def rotate_left(self):
        if self == None:
            return False
        if self.right == None:
            return False

        # Rotating
        t1 = self.right
        t2 = t1.left
        t1.left = self
        self.right = t2
        
        t1.assign_heights()
        return t1

    def double_rotate_left(self):
        if self == None:
            return None
        if self.right == None:
            return self
        
        self.right = self.right.rotate_right()
        return self.rotate_left()
    
    def double_rotate_right(self):
        if self == None:
            return None
        if self.left == None:
            return self

        self.left = self.left.rotate_left()
        return self.rotate_right()

    def balance(self):
        if self == None:
            return None

        bf = self.balance_factor()
        bf_L = 0
        bf_R = 0
        # need to call the these first so that we start at the bottom
        # of the bottom of the tree and work our way up
        # otherwise it wont stay an AVL tree 
        if self.left != None:
            self.left.balance()
            bf_L = self.left.balance_factor()
        if self.right != None:
            self.right.balance() 
            bf_R = self.right.balance_factor()
        
        if bf < -1:             # root is left heavy 
            if bf_L > 0:        # left child is right heavy
                self.left = self.left.rotate_left()
            return self.rotate_right()
        
        elif bf > 1:            # root is right heavy
            if bf_R < 0:        # right child is left heavy
                self.right = self.right.rotate_right()
            return self.rotate_left()
        
        return self

    def Add_in_order_rec(self, head, val):
        # Error Case
        if self == None:
            return None
        
        if self.val > val:
            # Base Case
            if self.left == None:
                self.left = AVL_tree(val)
                head.assign_heights()
                #head.Print_DepthFirst_more()
                head = head.balance()
                return head
            # recursion
            return self.left.Add_in_order_rec(head, val)
        elif self.val < val:
            # Base case
            if self.right == None:
                self.right = AVL_tree(val)
                head.assign_heights()
                #head.Print_DepthFirst_more()
                head = head.balance()
                return head
            # recursion
            return self.right.Add_in_order_rec(head, val)

    def Add_in_order(self, val):
        return self.Add_in_order_rec(self, val)
    
    def Print_DepthFirst_more(self):
        def rec(x,indent):
            print indent + str(x.val) + ", " + str(x.height) + ", " + str(x.balance_factor())
            indent += "\t"
            if x.right != None:
                rec(x.right,indent)
            if x.left != None:
                rec(x.left,indent)
            return True

        return rec(self,"")

# Testing
"""
root = AVL_tree(-10)
root = root.Add_in_order(0)
root = root.Add_in_order(10)
root = root.Add_in_order(20)
root = root.Add_in_order(30)
root = root.Add_in_order(40)
root = root.Add_in_order(50)
root = root.Add_in_order(60)
root = root.Add_in_order(70)
root = root.Add_in_order(80)
"""

root = AVL_tree(-10)
root = root.Add_in_order(0)
root = root.Add_in_order(10)
root = root.Add_in_order(20)
root = root.Add_in_order(30)

print
print "Print Depth"
root.Print_DepthFirst()

print
root.Print_DepthFirst_more()

# Testing the Balance function
"""
root = AVL_tree(-10)
root.Add_in_order(0)
root.Add_in_order(10)

print
print "Print Depth"
root.Print_DepthFirst()

print
root.Print_DepthFirst_more()

print
print "Balancing Root"
root = root.balance()
root.Print_DepthFirst_more()
"""

# Testing adding to the tree and left and right rotate functions
#   comment out head.balance() in the Add_in_order method
"""
root = AVL_tree(40)
root.Add_in_order(30)
root.Add_in_order(60)
root.Add_in_order(50)
root.Add_in_order(20)

print
print "Print Depth"
root.Print_DepthFirst()

print
root.Print_DepthFirst_more()

print
print "Left Rotate"
root = root.rotate_left()
root.Print_DepthFirst_more()

print
print "Right Rotate"
root = root.rotate_right()
root.Print_DepthFirst_more()
"""


