import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def simulate_brownian(T, n_steps, cov=np.identity(1)):
    L = np.linalg.cholesky(cov)
    dt = T/n_steps
    d = cov.shape[0]
    V = np.zeros([d, n_steps+1])
    eps = np.random.randn(d, n_steps)
    for i in range(0, n_steps):
        V[:,i+1] = V[:,i] + np.sqrt(dt)*L @ eps[:,i]
    return V

# Define a 3D covariance matrix with some correlation
rho12 = 0.3  # Correlation between dimensions 1 and 2
rho13 = 0.2  # Correlation between dimensions 1 and 3
rho23 = 0.4  # Correlation between dimensions 2 and 3

P = np.array([[1, rho12, rho13], 
              [rho12, 1, rho23], 
              [rho13, rho23, 1]])

# Simulate 3D Brownian motion
W = simulate_brownian(1, 5000, P)

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(W[0,:], W[1,:], W[2,:], linewidth=0.8)
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$x_3$')
ax.set_title('3D Brownian Motion')

# Show the plot
plt.tight_layout()
plt.show()
