from mpmath import *
import pylab as plt
mp.dps = 40

def f(x):
    return x**6 + x**3 + 2*x

def df(x):
    return 6*x**5 + 3*x**2 + 2

# O(h) precision
def df1(x, h):
    return (f(x + h) - f(x)) / h

# O(h^2) precision
def df2(x, h):
    return (f(x + h) - f(x - h)) / (2*h)

# Richardson extrapolation: O(h^4)
def df3(x, h):
    return (4*df2(x, h) - df2(x, 2*h)) / 3

def good_digits(x, h, der):
    dif = der(x, h) - df(x)
    return float(-log(abs(dif))/log(10))

xdense = arange(0, 40, .1)
plt.plot(xdense, [good_digits(1, 10**-x, df3) for x in xdense])
plt.show()
