# default step size
dx = .001

# O(h) precision
def dh1(f, x, h=dx):
    return (f(x + h) - f(x)) / h

# O(h^2) precision
def dh2(f, x, h=dx):
    return (f(x + h) - f(x - h)) / (2*h)

# Richardson extrapolation: O(h^4)
def dh4(f, x, h=dx):
    return (4 * dh2(f, x, h) - dh2(f, x, 2*h)) / 3