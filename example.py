 from pprint import pprint
import numpy as np

def jacobi(A, b, x=None, tol=None, n=None):
    """Solves the equation Ax=b via the Jacobi iterative method."""
    # Create an initial guess if needed                                                                                                                                                            
    if x is None:
        x = zeros(len(A[0]))

    # Create a vector of the diagonal elements of A                                                                                                                                                
    # and subtract them from A                                                                                                                                                                     
    D = np.diag(A)
    R = A - np.diagflat(D)

    # Iterate for N times                                                                                                                                                                          
    for i in range(n):
        x = (b - np.dot(R,x)) / D
        print(x)

    return x

A = np.array([[5, -2, 3], [-3, 9, 1], [2, -1, -7]])
b = np.array([-1, 2, 3])
XO = np.zeros(3)
n = 6

sol = jacobi(A,b,x=XO,n=n)

print ("A:")
pprint(A)

print ("b:")
pprint(b)

print ("x:")
pprint(sol)
	


# def seidel(a, x, b):
# 	n = len(a)
# 	for i in range(0,n):
# 		for j in range(0,n):
# 			if(i != 1):
# 				x[i] -= a[i][j] * x[j] + b[i]
# 				x[i] /= a[i][j]
# 		# 	err = (x[j]-x/x[j])
# 		# err = abs((x-x_prev)/x)
# 		print(x)

# 	return x

# n = 3
# # a = []
# # b = []

# x = [0,0,0]
# a = [[5, -2, 3], [-3, 9, 1], [2, -1, -7]]
# b = [-1, 2, 3]

# for i in range (0,100):
# 	x = seidel(a,x,b)
# 	print(x)