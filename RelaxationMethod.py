from numpy import *
import matplotlib.pyplot as plt

def relaxation(init, size_x, size_y):
    res = init[:]
    for x in range(1, size_x-1):
        for y in range(1, size_y-1):
            res[x,y] = (init[x-1,y] + init[x+1,y] + init[x,y-1] + init[x,y+1])/4
    return res

sx = 14
sy = 16
initial = array([[20] * sy]*sx)
for i in range(1,7):
    initial[0,i] = 10
for i in range(8,13):
    initial[sx-1, i] = 0
for _ in range(12):
    initial = relaxation(initial, sx, sy)
    plt.matshow(initial)
    plt.colorbar()
    plt.show()