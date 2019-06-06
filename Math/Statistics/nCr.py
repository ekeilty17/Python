def factorial(x):
    if x < 2:
        return 1
    return x * factorial(x-1)

def nCr(n, r):
    #return factorial(n)/( factorial(r) * factorial(n-r) )
    if r < 0 or r > n:
        return 0
    if r == 0 or r == n:
        return 1
    if r == 1 or r == (n-1):
        return n

    # More efficient code
    accum = 1
    for i in range(n, 1, -1):
        if i > (n-r):
            accum *= i
        if i <= r:
            accum /= i
    return accum
