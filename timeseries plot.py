import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ========== PARAMETERS for second system ==========
params = {
    'a0': 0.01,
    'a': 9.0,
    'k1': 3,
    'k0': 0,
    'd1': 1,
    'b0': 0.01,
    'b': 9.0,
    'k2': 3,
    'd2': 1,
    'g': 1.0,
    'k3': 2
}

# ========== SYSTEM DEFINITION ==========
def system(t, vars, params):
    x, y = vars
    a0, a, k1, k0, d1 = params['a0'], params['a'], params['k1'], params['k0'], params['d1']
    b0, b, k2, d2, g, k3 = params['b0'], params['b'], params['k2'], params['d2'], params['g'], params['k3']
    
    dxdt = a0 + (a * y**2) / ((k1 - k0)**2 + y**2) - d1 * x
    dydt = b0 + (b * x**2) / (k2**2 + x**2) - d2 * y + (g * y**2) / (k3**2 + y**2)
    return [dxdt, dydt]

# ========== SOLVE ODEs ==========
# Initial conditions
x0, y0 = 0, 0

# Time span
t_span = (0, 100)
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# Solve system
sol = solve_ivp(system, t_span, [x0, y0], args=(params,), t_eval=t_eval)

# ========== PLOT ==========
plt.figure(figsize=(10, 5))
plt.plot(sol.t, sol.y[0], label='x(t)')
plt.plot(sol.t, sol.y[1], label='y(t)')
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Time Series for IL-36 AND TH-17 sysytem')
plt.legend()
plt.grid(True)
plt.show()
