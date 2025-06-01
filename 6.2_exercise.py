import numpy as np
import matplotlib.pyplot as plt
from math import *



T = 2*pi
n_steps = 1000
dt = T/n_steps
U = np.zeros(n_steps +1)
V = np.zeros(n_steps +1)
U[0]= 1
V[0]= 0

for i in range(0,n_steps):
    U[i+1] = U[i] + V[i]*dt
    V[i+1] = V[i] - U[i]*dt

ax = plt.gca()
ax.plot(U,V)
ax.set_aspect('equal')

plt.show()


