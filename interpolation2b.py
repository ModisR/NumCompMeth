from interpolation2 import plot
from numpy import cos, pi


def cheb(a, b, n):
    pts = [cos(i * pi / n) for i in range(n)]
    return [((a + b) + (a - b) * p) / 2 for p in pts]


plot(cheb(-10, 10, 20))
