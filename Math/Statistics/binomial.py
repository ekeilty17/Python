import numpy as np
import matplotlib.pyplot as plt
from nCr import nCr

# mean = np
# variance = np(1-p)
def b(x, n, p, plot=False):
    # n = number of Bernoulli trials preformed
    # x = number of successes in n Bernoulli trials
    # p = probability of a success in the Bernoulli trial
    if x > n:
        raise TypeError("x must be less than or equal to n, since n is the total number of trials and x is the number of successes.")
    if not (0 <= p <= 1):
        raise TypeError("p is a probability and needs to be in [0, 1]")
    
    
    xx = range(n+1)
    yy = [nCr(n, i) * p**i * (1-p)**(n-i) for i in xx]
    plt.bar(xx, yy, align='center', width=1.0, edgecolor='black')
    plt.xticks(xx, xx)
    plt.xlabel("x")
    plt.ylabel("b(x; n, p)")
    plt.title("Binomial Distribution")
    if plot:
        plt.show()
    
    return nCr(n, x) * p**x * (1-p)**(n-x)

def B(r, n, p, plot=False):
    #B(r, n, p) = b(0, n, p) + b(1, n, p) + ... + b(r-1, n, p) + b(r, n, p)
    
    rr = range(n+1)
    yy = [(1-p)**(n)]           #b(0, n, p)
    for i in range(1,n+1):
        yy += [yy[-1] + nCr(n, i) * p**i * (1-p)**(n-i)]

    plt.bar(rr, yy, align='center', width=1.0, edgecolor='black')
    plt.xticks(rr, rr)
    plt.xlabel("r")
    plt.ylabel("B(r; n, p)")
    plt.title("Cumulative Binomial Distribution")
    if plot:
        plt.show()
    
    return yy[-1]

def b_star(x, k, p, plot=False):
    # k = number of successes 
    # x = number of Bernoulli trials required to produce k successes
    # p = probability of a success in the Bernoulli trial
    if k > x:
        raise TypeError("x must be greater than or equal to k, since x is the number of trials required to produce k successes.")
    if not (0 <= p <= 1):
        raise TypeError("p is a probability and needs to be in [0, 1]")
    
    xx = range(k, 100)
    yy = [nCr(i-1, k-1) * p**k * (1-p)**(i-k) for i in xx]
    plt.bar(xx, yy, align='center', width=1.0, edgecolor='black')
    plt.xticks(xx, xx)
    plt.xlabel("x")
    plt.ylabel("b*(x; k, p)")
    plt.title("Negative Binomial Distribution")
    if plot:
        plt.show()
    
    return nCr(x-1, k-1) * p**k * (1-p)**(x-k)

# mean = 1/p
# variance = (1-p)/p**2
def g(x, p, plot=False):
    # x = number of Bernoulli trials required to produce 1 success
    # p = probability of a success in the Bernoulli trial
    return b_star(x, 1, p, plot)

B(5, 10, 0.2, True)
