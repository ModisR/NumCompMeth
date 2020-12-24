from numpy import *
from matplotlib.pyplot import *

def normal2(sigma):
    n1 = random.normal(0, sigma)
    n2 = random.normal(0, sigma)
    return array([n1, n2])

def stochastic(sigma):
    t1 = 1
    dt = .001
    sdt = sqrt(dt)
    ts = arange(0, t1, dt)
    xs = [array([0, 0])]
    for _ in ts:
        x = xs[-1] + sigma*normal2(sdt)
        xs = append(xs, [x], axis=0)
    ts = append(ts, t1)
    return ts, xs

for i in range(5):
    _, xs = stochastic(1)
    x1 = [x[0] for x in xs]
    x2 = [x[1] for x in xs]
    plot(x1, x2, alpha=0.5)
axes().set_aspect('equal', 'datalim')
show()

x1s = zeros(1000)
x2s = zeros(1000)
for i in range(1000):
    _, xs = stochastic(1)
    x1s[i], x2s[i] = xs[-1]
plot(x1s, x2s, "o", alpha=.5)
show()