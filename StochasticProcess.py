from numpy import *
import matplotlib.pyplot as plt


def brownian(t1, sigma):
    dt = .001
    sdt = sqrt(dt)
    ts = arange(0, t1, dt)
    xs = [0]
    for _ in ts:
        x = xs[-1] + sigma * random.normal(0, sdt)
        xs.append(x)
    ts = append(ts, t1)
    return ts, xs


n = 500
ys = zeros(n)
for i in range(n):
    ts_, xs_ = brownian(1, 1)
    ys[i] = xs_[-1]

xtab = zeros(20)
for y in ys:
    xtab[int(2 * y + 10)] += 2/n

xs1 = arange(-5, 5, .5)
xs2 = arange(-5, 5, .1)
normal = [exp(-x*x/2)/sqrt(2*pi) for x in xs2]
plt.plot(xs2, normal)
plt.plot(xs1, xtab)
plt.show()
