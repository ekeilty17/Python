#I don't really believe in one-liners, I value readability
#nevertheless, these are fun to come up with

A = [[1,2,3,0], [4,5,6,0], [7,8,9,0]]
print A
print

#Flatten a Matrix
Flat = [A[x][y] for x in range(len(A)) for y in range(len(A[0]))]
print Flat
print

#Print a Matrix
for i in range(len(A)): print ' '.join(str(n) for n in [A[x][y] for x in range(len(A)) for y in range(len(A[0]))][ len(A[0])*i : len(A[0])*(i+1) ])
print

print '\n'.join("%i Byte = %i Bit = largest number: %i" % (j, j*8, 256**j-1) for j in (1 << i for i in xrange(8)))
