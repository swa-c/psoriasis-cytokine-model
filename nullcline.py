import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.linalg import eigvals

# Define parameter values
params = {
    'a0': 0.01,    
    'a': 9.0,      
    'k1': 3,       
    'd1': 1,       
    'b0': 0.01,    
    'b': 9.0,      
    'k2': 3,       
    'd2': 1,       
    'g': 0.1,      
    'k3': 5      
}

# Define the system of equations
def equations(vars):
    x, y = vars
    dxdt = params['a0'] + (params['a'] * y**2) / (params['k1']**2 + y**2) - params['d1'] * x
    dydt = params['b0'] + (params['b'] * x**2) / (params['k2']**2 + x**2) - params['d2'] * y + (params['g'] * y**2) / (params['k3']**2 + y**2)
    return [dxdt, dydt]

# Find steady states numerically
steady_states = []
initial_guesses = [[1, 1], [2, 2], [3, 3], [5, 5]]  # Added a guess for the third intersection
for guess in initial_guesses:
    solution = fsolve(equations, guess)
    steady_states.append(solution)

# Remove duplicate steady states (if any)
steady_states = np.unique(np.round(steady_states, decimals=5), axis=0)

# Analyze stability using the Jacobian matrix
def stability_analysis(x, y):
    # Jacobian matrix of the system
    J = np.array([
        [-params['d1'], (2 * params['a'] * y) / (params['k1']**2 + y**2) - (2 * params['a'] * y**3) / (params['k1']**2 + y**2)**2],
        [(2 * params['b'] * x) / (params['k2']**2 + x**2) - (2 * params['b'] * x**3) / (params['k2']**2 + x**2)**2, -params['d2'] - (2 * params['g'] * y) / (params['k3']**2 + y**2) + (2 * params['g'] * y**3) / (params['k3']**2 + y**2)**2]
    ])
    
    eigenvalues = eigvals(J)
    # If eigenvalues have negative real part, it's stable
    if np.all(np.real(eigenvalues) < 0):
        return 'stable'
    else:
        return 'unstable'

# Plot nullclines
y_values = np.linspace(0, 10, 100)
# x-nullcline: dxdt = 0
x_nullcline = (params['a0'] + (params['a'] * y_values**2) / (params['k1']**2 + y_values**2)) / params['d1']

# y-nullcline: dydt = 0
x_values = np.linspace(0, 10, 100)
y_nullcline = (params['b0'] + (params['b'] * x_values**2) / (params['k2']**2 + x_values**2) - (params['g'] * y_values**2) / (params['k3']**2 + y_values**2)) / params['d2']

# Plot nullclines
plt.plot(x_nullcline, y_values, label='x-nullcline', color='blue')
plt.plot(x_values, y_nullcline, label='y-nullcline', color='green')

# Add small points for steady states along the nullclines
for state in steady_states:
    x, y = state
    # Stability analysis
    stability = stability_analysis(x, y)
    # Plot stable points as green, unstable as red
    color = 'green' if stability == 'stable' else 'red'
    plt.plot(x, y, marker='o', markersize=6, color=color)

# Phase portrait
x = np.linspace(0, 10, 20)  # x range
y = np.linspace(0, 10, 20)  # y range
X, Y = np.meshgrid(x, y)  # Create a grid

# Compute derivatives at each grid point
DX, DY = np.zeros(X.shape), np.zeros(Y.shape)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        dxdt, dydt = equations([X[i, j], Y[i, j]])
        DX[i, j] = dxdt
        DY[i, j] = dydt

# Normalize the vectors for better visualization
magnitude = np.sqrt(DX**2 + DY**2)
DX_normalized = DX / magnitude
DY_normalized = DY / magnitude

# Plot the phase portrait using quiver
plt.quiver(X, Y, DX_normalized, DY_normalized, color='blue', angles='xy', scale_units='xy', scale=4, label='Phase Portrait')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Nullclines, Phase Portrait, and Stability of Steady States')
plt.grid()
plt.show()
