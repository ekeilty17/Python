import numpy as np
import matplotlib.pyplot as plt
import math

# These functions aren't meant to be useful
# Purpose is to just show the syntax

def BarGraph(categories, vals, x_label=None, y_label=None, title=None, color='b'):
    
    x_pos = np.arange(len(categories))
    plt.bar(x_pos, vals, align='center', color=color)
    
    plt.xticks(x_pos, categories)
    
    # Adding Labels
    if x_label != None:
        plt.xlabel(x_label)
    if y_label != None:
        plt.ylabel(y_label)
    if title != None:
        plt.title(title)
 
    plt.show()

#BarGraph(['A', 'B', 'C', 'D', 'E'], [10, 5, -4, 3, 2], title="Bar Graph") 


def Stem_and_Leaf(data, n=0, double=False):

    # Creating stem column
    stem = sorted(list(set([int(d/(10**n)) for d in data])))

    out = ""
    # Creating leaf column
    leaf = [[] for i in range(len(stem))]
    """This works, but for some reason int(9.0) = 8, probably something to do with binary idk
    for d in data:
        leaf[stem.index(int(d/(10**n)))] += [ d/(10**(n-1))%10 ]
    """
    for d in data:
        leaf[stem.index(int(d/(10**n)))] += [ int(str(d/(10**n))[-1]) ]
    for i in range(len(leaf)):
        leaf[i] = sorted(leaf[i])

    if not double:
        out += "Stem\tLeaf\n"
        for i in range(len(stem)):
            out += str(stem[i]) + '\t'

            temp = ''
            for l in leaf[i]:
                temp += str(l)
            out += temp + '\n'
    

    if double:
        partitioned_leaf = [[] for i in range(2*len(stem))]
        for i in range(0, len(partitioned_leaf), 2):
            partitioned_leaf[i] = [l for l in leaf[i/2] if l<5]
            partitioned_leaf[i+1] = [l for l in leaf[i/2] if l>4]
        
        out += "Stem\tLeaf\n"
        for i in range(2*len(stem)):
            out += str(stem[i/2])
            if i%2 == 0:
                out += '.\t'
            else:
                out += '*\t'

            temp = ''
            for l in partitioned_leaf[i]:
                temp += str(l)
            out += temp + '\n'

    return out

stem_and_leaf_data = [ 2.2, 4.1, 3.5, 4.5, 3.2, 3.7, 3.0, 2.6,
                       3.4, 4.6, 3.1, 3.3, 3.8, 3.1, 4.7, 3.7,
                       2.5, 4.3, 3.4, 3.6, 2.9, 3.3, 3.9, 3.1,
                       3.3, 3.1, 3.7, 4.4, 3.2, 4.1, 4.9, 3.4,
                       4.7, 3.8, 3.2, 2.6, 3.9, 3.0, 4.2, 3.5]

print Stem_and_Leaf(stem_and_leaf_data, double=True)

def Histogram(data, n_bins, x_label=None, y_label=None, title=None, color='b'):
    
    plt.hist(histogram_data, n_bins, color=color)
    
    # Adding Labels
    if x_label != None:
        plt.xlabel(x_label)
    if y_label != None:
        plt.ylabel(y_label)
    if title != None:
        plt.title(title)
    
    plt.show()

histogram_data = [ 2.2, 4.1, 3.5, 4.5, 3.2, 3.7, 3.0, 2.6,
                   3.4, 1.6, 3.1, 3.3, 3.8, 3.1, 4.7, 3.7,
                   2.5, 4.3, 3.4, 3.6, 2.9, 3.3, 3.9, 3.1,
                   3.3, 3.1, 3.7, 4.4, 3.2, 4.1, 1.9, 3.4, 
                   4.7, 3.8, 3.2, 2.6, 3.9, 3.0, 4.2, 3.5]

#Histogram(histogram_data, 15)

boxplot_data = [  1.09, 1.92, 2.31, 1.79, 2.28, 1.74, 1.47, 1.97,
                  0.85, 1.24, 1.58, 2.03, 1.70, 2.17, 2.55, 2.11,
                  1.86, 1.90, 1.68, 1.51, 1.64, 0.72, 1.69, 1.85,
                  1.82, 1.79, 2.46, 1.88, 2.08, 1.67, 1.37, 1.93,
                  1.40, 1.64, 2.09, 1.75, 1.63, 2.37, 1.75, 1.69]

def Boxplot(data, notched=False, color='r.', verticle=False, whiskers=1.5, x_label=None, y_label=None, title=None):
    
    plt.boxplot(boxplot_data, notched, color, verticle, whiskers)

    # Adding Labels
    if x_label != None:
        plt.xlabel(x_label)
    if y_label != None:
        plt.ylabel(y_label)
    if title != None:
        plt.title(title)

    plt.show()

#Boxplot(boxplot_data)

def Scatterplot(X, Y, size=50, color='b', x_label=None, y_label=None, title=None):
    
    plt.scatter(X, Y, s=size, c=color)
    
    # Adding Labels
    if x_label != None:
        plt.xlabel(x_label)
    if y_label != None:
        plt.ylabel(y_label)
    if title != None:
        plt.title(title)
    
    plt.show()

"""
X = range(20)
Y = [x**2 for x in X]
size = (30*np.random.rand(20))**2
color = np.random.rand(20)
Scatterplot(X, Y, size, color)
"""
