from numpy import *
import matplotlib.pyplot as plt

from lib.relaxation import relaxation

sx = 16
sy = 16
solution = array([[1.] * sy]*sx)

for i in range(16):
    # here we put the right boundary conditions
    solution[0, i] = 1
    solution[i, 0] = 1
    solution[15, i] = 2
    solution[i, 15] = 2

for _ in range(20):
    solution = relaxation(solution, sx, sy, 1, 3)
    plt.matshow(solution)
    plt.colorbar()
    plt.show()