from matplotlib import pyplot as plt
from numpy import arange

from lib.interpolation import lagrange


xs = [1, 2, 3, 4, 5, 6]
ys = [0, 0.841471, 0.909297, 0.14122, -0.756902, -0.958924]
xdense = arange(0, 7, .1)
ydense = [lagrange(x, ys, xs) for x in xdense]

plt.plot(xs, ys, 'ro')
plt.plot(xdense, ydense)
plt.show()
