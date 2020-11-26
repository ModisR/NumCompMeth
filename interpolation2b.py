from interpolation2 import plot, fun
from numpy import *


def cheb(a, b, n):
    pts = [cos((i + .5) * pi / n) for i in range(n)]
    return [((a + b) + (a - b) * p) / 2 for p in pts]


plot(cheb(-10, 10, 20))
