from numpy import *
from matplotlib.pyplot import *

def stochastic(sigma):
    dt = .001
    sdt = sqrt(dt)
    t1 = 10
    ts = arange(0, t1, dt)
    xs = [0]
    for t in ts:
        x = xs[-1] + dt*cos(t) + random.normal(0, sigma*sdt)
        xs = append(xs, x)
    ts = append(ts, t1)
    return ts, xs

for sig in arange(.2, 1.2, .2):
    tz, xz = stochastic(sig)
    plot(tz, xz, alpha=.5)
show()