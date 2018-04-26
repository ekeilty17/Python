from matrix import *
from GE import *

def LI(V):
    #V is a set of vectors
    if not isMatrix(V):
        return False
    
    #it's trippy bc I need to represent them using row vectors but they are column vectors
    V = transpose(V)
    #add a zero column so the GE works
    z = [0]*len(V)
    V_ = GE(aug(V,z))
    #check if the result of GE is the idenity augmented with a zero column
    if V_ == aug(Iden(len(V)),z):
        return True
    else:
        return False

v1 = [1,0,0]
v2 = [0,1,0]
v3 = [0,0,1]

print LI([v1,v2,v3])
