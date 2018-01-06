def bubblesort(inp):

    try:
        A = list(inp)
    except:
        return False
    
    if A == []:
        return False
    if len(A) == 1:
        return False
    
    for i in A:
       if (type(i) != int):
           return False

    swapped = True
    while swapped:
        swapped = False
        for i in range(1,len(A)):
            if (A[i-1] > A[i]):
                temp = A[i-1]
                A[i-1] = A[i]
                A[i] = temp
                swapped = True
    return [True, A]
