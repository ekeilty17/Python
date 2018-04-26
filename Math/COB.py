from matrix import *

def ChangeOfBasis(e,f):
    #e is a list of the coordinates of basis E
    #f is a list of the coordinates of basis F
    #   the e & f matrices are gonna be weird bc in Math they are col vectors
    #   but we will have to represent them with row vectors
    #   so basically e and f are matrices
    if not isMatrix(e) or not isMatrix(f):
        return False
    #need to check if e and f are actually bases
    #I can't check that it spans the vector space bc I don't know the vector space
    #I can check that the dimensions match
    if len(e) != len(f):
        return False
    for i in range(0,len(e)):
        if len(e[i]) != len(f[i]):
            return False
    #and check that they are linearly independent


    #Okay so we have 2 arbitrary bases
    #we need the COB matrix from the standard basis to e and f
