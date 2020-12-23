from numpy import *

def golden(a, b, f):
    alpha = (3-sqrt(5))/2
    x1,x2 = a+alpha*(b-a), b-alpha*(b-a)
    y = x1
    while abs(f(x1) - f(x2)) > 10**-4:
        if f(x1) > f(x2):
            a, y = x1, x2
        else:
            b, y = x2, x1
        x1, x2 = a+alpha*(b-a), b-alpha*(b-a)
    return y