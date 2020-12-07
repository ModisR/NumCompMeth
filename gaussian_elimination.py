from numpy import *

def solve(A, b):
    n = len(A)
    # Elimination phase
    for i in range(n-1):
        # Choose pivot with largest entry
        for j in range(i+1, n):
            if abs(A[j,i]) > abs(A[i,i]):
                (A[i], A[j]) = (copy(A[j]), copy(A[i]))
                (b[i], b[j]) = (copy(b[j]), copy(b[i]))
        # Eliminate i-th terms
        for j in range(i+1, n):
            factor = A[j,i] / A[i,i]
            A[j] = A[j] - factor * A[i]
            b[j] = b[j] - factor * b[i]
    # Substitution phase
    x = copy(b)
    for i in range(n-1, -1, -1):
        x[i] -= A[i, i+1:].dot(x[i+1:])
        x[i] /= A[i,i]
    return x

A0 = array([[-2., 1., 0., -1.], [1., -2., 4., 0.], [-3., 4., 1., 0.], [-1., 3., 0., 1.]])
b0 = array([19., 43., 40., 20.])
x1 = solve(A0, b0)
print(x1)
