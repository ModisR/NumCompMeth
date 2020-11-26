from numpy import *
from matplotlib import pyplot as plt
from scipy.linalg import expm

h = .4
y0 = array([1, 1])
# uses RK4 to solve y' = F(x, y) on [0, x]
# with sub-interval h
# and initial condition y(0) = y0
def Integrator(F, x):
    y = y0
    ys = [y0]
    for x in arange(h, x + h, h):
        def sample(dx, grad):
            return F(x + dx, y + dx * grad)
        k0 = F(x, y)
        k1 = sample(h/2, k0)
        k2 = sample(h/2, k1)
        k3 = sample(h, k2)
        y = y + h * (k0 + 2*(k1 + k2) + k3) / 6
        ys.append(y)
    return ys


A = array([[2, 3], [0, -2]])
def f(_, y):
    return A.dot(y)


end = 2
xs = arange(0, end + h, h)
ys = Integrator(f, end)
xdense = arange(0, end + .1, .1)
ydense = [expm(A * x).dot(y0) for x in xdense]

plt.plot(xs, ys)
plt.plot(xdense, ydense)
plt.show()
