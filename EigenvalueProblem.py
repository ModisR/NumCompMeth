from numpy import *

from lib.root_finding import newton as newton
from lib.jacobi_eigenvalues import diagonalise

A = array([[1.,-1.,0.], [-1.,4.,-2.], [0.,-2.,2.]])
def det_l(la):
    return linalg.det(A - la*identity(3))

for x0 in [0, 1, 5]:
    print(newton(det_l, x0))

print(diagonalise(A))