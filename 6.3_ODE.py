import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the ODE as a Python function
def dydt(t, y):
    return -2 * y

# Time span and initial condition
t_span = (0, 5)       # from t=0 to t=5
y0 = [1]              # initial value y(0) = 1

# Solve the ODE
solution = solve_ivp(dydt, t_span, y0, t_eval=np.linspace(0, 5, 100))

# Plot the result
plt.plot(solution.t, solution.y[0], label="y(t)")
plt.title("Solution of dy/dt = -2y")
plt.xlabel("Time t")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
