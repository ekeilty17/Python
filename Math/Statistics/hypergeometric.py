import numpy as np
import matplotlib.pyplot as plt
from nCr import nCr

# mean = nk/N
# variance = (N-n)/(N-1) * n * (k/N) * (1-k/N)
def h(x, N, n, k, plot=False):
    # N = total number of objects
    # n = number of trials or sample size
    # k = number of objects labeled a success
    # x = number of objects picked in n trials that are labeled a success
    if n > N:
        raise TypeError("n must be less than or equal to N, since N is the total number of objects and n is the number of trials performed.")
    if k > N:
        raise TypeError("k must be less than or equal to N, since N is the total number of objects and k is the number of objects that are labeled successes.")
    if x > N:
        raise TypeError("x must be less than or equal to N, since N is the total number of objects and x is the nummber of successes.")
    if x > n:
        raise TypeError("x must be less than or equal to n, since N is the total number of objects and x is the nummber of successes.")
    
    if plot:
        xx = range( max(0, n-(N-k)), min(n,k)+1 )
        yy = [( nCr(k, i) * nCr(N-k, n-i) ) / float(nCr(N, n)) for i in xx]
        plt.bar(xx, yy, align='center', width=1.0, edgecolor='black')
        plt.xticks(xx, xx)
        plt.xlabel("x")
        plt.ylabel("h(x; N, n, k)")
        plt.title("Hypergeometric Distribution")
        plt.show()
    
    return ( nCr(k, x) * nCr(N-k, n-x) ) / float(nCr(N, n))

def h_interval(a, b, N, n, k, plot=False):
    accum = 0
    for i in range(a, b+1):
        accum += h(i, N, n, k)
    
    h(a, N, n, k, plot)

    return accum

def h_range(x, N, n, k):
    
    # if n > N-k (number of failtures), then you have to at least choose n-(N-k) successes,
    #                                   therefore x in [n-(N-k), ...] 
    # if k > n, then you can't pick more than n successes, therefore x in [..., n]
    # Otherwise the intutive range of [0, k] applies
    return [max(0, n-(N-k)), min(n,k)]

