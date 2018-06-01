#Linear Algebra Code
This code preforms common operations one would do in a first year linear algebra course such as Gaussian Elimination, checking if a set of vectors are linearly independent, and Change of Basis.

##Matrix
In essense a matrix is just a 2D list. Here is the list of methods associated with the matrix object.

* .get()
* .setRow(r)
* .setCol(c)
* .deleteRow(r)
* .deleteCol(c)
* .set(L)
* .copy()
* .dim()
* .isSquare()
* .scale(k)
* .transpose()
* .submatrix()
* .Det()
* .minor()
* .cof()
* .cofactor\_matrix()
* .adj()
* .inverse()

Moreover I can preform operations between matrices such as add, subtract, multiply, and augment.

###Matrix Properties
There are many important types of matrices. The file `matrix_prop.py` contains functiosn to check or produce special types of matrices.  

##Vector
In essense a vector is just a 1D list. Here are some of the methods associated with the vector object.

* .get()
* .set(L)
* .copy()
* .dim()
* .scale(k)
* .magnitude()
* .normalize()

Moreover I can preform operations between vectors such as add, substract, dot product, cross product, angle between, and projection onto.

##Operations between vectors are matrices
The relationship between vectors and matrices are the core of linear algebra. I have a series of functions that convert one object to another and make preforming operations between them much easier.

* vector\_list\_to\_matrix(L)
* matrix\_to\_list\_vectors(A)
* vector\_to\_matrix(v)
* matrix\_to\_vector(A)
* matrix\_vector\_multiply(A, v)

##Linear Algebra Concepts
Now that I have created the basics, I can implement core concepts in Linear Algebra such as

* Gaussian Elimination
* Checking if vectors are Linearly Independent
* Generating a Change of Basis Matrix and Preforming Change of Basis on a Linear Transformation
