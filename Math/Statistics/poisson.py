from scipy.integrate import quad
from scipy.special import gamma
import numpy as np
import matplotlib.pyplot as plt

# mean = Lt
# variance = Lt
def p(x, Lt, plot=False):
    # x = number of outcomes occuring in a given time interval or spacial region
    # L = lambda = rate of occurence of outcomes
    # t = specific time of interest
    if x < 0:
        raise TypeError("x must be a positive integer")
    
    xx = np.arange(0, 20, 1)
    yy = np.exp(-Lt) * (Lt)**xx / gamma(xx+1)

    if plot:
        plt.plot(xx, yy)
        plt.xlabel("x")
        plt.ylabel("")
        plt.title("Poisson Distribution")
        plt.show()

    return np.exp(-Lt) * (Lt)**x / float(np.math.gamma(x+1))


def P(r, Lt):
    """
    def p_integrand(x):
        return p(x, Lt)
    ans, err = quad(p_integrand, 0, r)
    return ans
    """
    accum = 0
    for i in range(r+1):
        accum += p(i, Lt)
    return accum

def P_interval(a,b, Lt):
    """
    def p_integrand(x):
        return p(x, Lt)
    ans, err = quad(p_integrand, a, b)
    return ans
    """
    accum = 0
    for i in range(a, b+1):
        accum += p(i, Lt)
    return accum

print p(3, 500*0.01, True)
#print 1 - P(14, 500*0.01)
#print P_interval(6,8, 10)
