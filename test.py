from math import *
n = 10000
accum = 0
neg = 1

for i in range(1,n):
    accum += neg*(1/float(i))
    neg *= -1
    print accum

print
print log(2,e)
