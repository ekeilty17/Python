import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def normal(u, sigma, plot=True):

    u = float(u)
    sigma = float(sigma)

    x = np.arange(u - 5*sigma, u + 5*sigma, 0.001 * sigma)
    n = 1.0/(np.sqrt(2 * np.pi) * sigma) * np.exp( - 1.0/(2*sigma**2) * (x - u)**2)

    L = "Mean = " + str(u) + ", StdDev = " + str(sigma)
    plt.plot(x, n, label=L)
    plt.xlabel("x")
    plt.ylabel("")
    plt.title("Normal Distribution")
    if plot:
        plt.legend(loc='upper right')
        plt.show()

    return [u, sigma]

def N(a, b, u, sigma, plot=False):

    a = float(a)
    b = float(b)
    u = float(u)
    sigma = float(sigma)

    x = np.arange(u - 5*sigma, u + 5*sigma, 0.001 * sigma)
    n = 1.0/(np.sqrt(2 * np.pi) * sigma) * np.exp( - 1.0/(2*sigma**2) * (x - u)**2)
    
    L = "Mean = " + str(u) + ", StdDev = " + str(sigma)
    plt.plot(x, n, label=L)
    plt.fill_between(x, n, 0, where= (x>=a) & (x<=b), color='r')
    plt.xlabel("x")
    plt.ylabel("")
    plt.title("Normal Distribution")
    
    def nn(x):
        return 1.0/(np.sqrt(2 * np.pi) * sigma) * np.exp( - 1.0/(2*sigma**2) * (x - u)**2)
    
    area = quad(nn, a, b)
    print area
    
    if plot:
        plt.legend(loc='upper right')
        plt.show()
    
    return area

def z(x, u, sigma):
    return (x - u)/float(sigma)

def standard_normal(plot=True):
    return normal(0, 1, plot)

def Z(a, b, plot=False):
    return N(a, b, 0, 1, plot)

N(7960, np.inf, 7950, 20, True)
