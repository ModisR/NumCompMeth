from numpy import *

def rem_kl(l, k, A):
    t = 2*A[k,l]/(A[l,l] - A[k,k])
    c = sqrt((1 + sqrt(1/(1 + t*t)))/2)
    s = (1 - 2*c*c) * A[k,l] / c / (A[k,k] - A[l,l])
    n = A[0].size
    B = A.copy()
    for i in range(n):
        B[k,i] = c*A[k,i]-s*A[l,i]
        B[i,k] = B[k,i]
        B[l,i] = c*A[l,i]+s*A[k,i]
        B[i,l] = B[l,i]
    B[k,l] = 0
    B[l,k] = 0
    B[k,k] = c*c * A[k,k] + s*s * A[l,l] - 2*c*s * A[k,l]
    B[l,l] = c*c * A[l,l] + s*s * A[k,k] + 2*c*s * A[k,l]
    return B

def find_max(A):
    imax = 0
    jmax = 1
    max_val = abs(A[0,1])
    n = A[0].size
    for i in range(n):
        for j in range(i+1,n):
            if abs(A[i,j]) > max_val:
                imax, jmax = i, j
                max_val = abs(A[i,j])
    return imax, jmax, max_val

def diagonalise(A):
    B = A.copy()
    max_c = 1
    while max_c > 10**-6:
        i, j, max_c = find_max(B)
        B = rem_kl(i, j, B)
    return B