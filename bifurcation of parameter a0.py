import PyDSTool as dst
import numpy as np
from matplotlib import pyplot as plt

print("Starting saddle-node bifurcation analysis...")

# ---------- Parameters for your system (added g and k3 for self-loop) ----------
DSargs = dst.args(name='Saddle-Node Bifurcation Analysis')
DSargs.pars = {
    'a0': 0.01,    
    'a': 5.5,      
    'k1': 3.0,    
    'd1': 1.0,     
    'b0': 0.01,    
    'b': 5.5,      
    'k2': 3.0,  
    'd2': 1.1,     
    'g': 1.5,     
    'k3': 3.0     
}

# ---------- RHS of your differential equations (y has added self-loop) ----------
DSargs.varspecs = {
    'x': 'a0 + (a * y**2 / (k1**2 + y**2)) - d1 * x',
    'y': 'b0 + (b * x**2 / (k2**2 + x**2)) - d2 * y + (g * y**2 / (k3**2 + y**2))'
}

# Initial conditions and time domain
DSargs.ics = {'x': 0, 'y': 0}
DSargs.tdomain = [0, 100]

# Create the ODE system
print("Creating ODE system...")
ode = dst.Generator.Vode_ODEsystem(DSargs)

# ---------- Continuation analysis ----------
print("\n=== Bifurcation Analysis ===")
PC = dst.ContClass(ode)

# First continuation: vary parameter 'a0'
PCargs = dst.args(name='EQ1', type='EP-C')
PCargs.freepars = ['a0']          # Now we vary a0
PCargs.MaxNumPoints = 1000
PCargs.MaxStepSize = 0.1
PCargs.MinStepSize = 1e-6
PCargs.StepSize = 0.05
PCargs.LocBifPoints = 'LP'
PCargs.SaveEigen = True
PCargs.StopAtPoints = 'B'
PC.newCurve(PCargs)

# Compute the curve
print("Computing equilibrium curve while varying parameter 'a0'...")
PC['EQ1'].forward()
PC['EQ1'].backward()

# Plot bifurcation diagrams
print("Plotting bifurcation diagrams...")
plt.figure()
PC.display(['a0', 'x'], stability=True)
plt.xlabel('Parameter a0')
plt.ylabel('x equilibrium')
plt.title('Bifurcation diagram: x vs a0')
plt.grid()
plt.show()

plt.figure()
PC.display(['a0', 'y'], stability=True)
plt.xlabel('Parameter a0')
plt.ylabel('y equilibrium')
plt.title('Bifurcation diagram: y vs a0')
plt.grid()
plt.show()

# ---------- Check for saddle-node bifurcations ----------
print("\n=== Checking for Saddle-Node Bifurcations ===")
if hasattr(PC['EQ1'], 'getSpecialPoint'):
    try:
        LP = PC['EQ1'].getSpecialPoint('LP1')
        if LP is not None:
            print(f"\n*** SADDLE-NODE BIFURCATION FOUND ***")

            # Correct way to access parameter and variable values
            param_index = PC['EQ1'].freepars.index('a0')
            x_index = ode.funcspec.vars.index('x')
            y_index = ode.funcspec.vars.index('y')

            print(f"Found at parameter value a0 = {LP.coordarray[param_index]:.6f}")
            print(f"Corresponding equilibrium values:")
            print(f"x = {LP.coordarray[x_index]:.6f}")
            print(f"y = {LP.coordarray[y_index]:.6f}")

            # Continue the limit point in two parameters (a0 and a)
            print("\nContinuing the saddle-node bifurcation in (a0, a) space...")
            PCargs = dst.args(name='SN1', type='LP-C')
            PCargs.initpoint = 'EQ1:LP1'
            PCargs.freepars = ['a0', 'a']
            PCargs.MaxStepSize = 0.1
            PCargs.LocBifPoints = []
            PCargs.MaxNumPoints = 100
            PC.newCurve(PCargs)

            PC['SN1'].forward()
            PC['SN1'].backward()

            # Plot the curve of saddle-node bifurcations
            plt.figure()
            PC['SN1'].display(['a0', 'a'])
            plt.xlabel('a0')
            plt.ylabel('a')
            plt.title('Curve of saddle-node bifurcations')
            plt.grid()
            plt.show()

            print("Completed continuation of saddle-node bifurcation curve.")
        else:
            print("\nNo saddle-node bifurcations found while varying parameter 'a0'.")
    except Exception as e:
        print(f"\nError while checking for limit points: {str(e)}")
else:
    print("\nNo special points (including saddle-node bifurcations) were found.")

print("\nAnalysis complete.")
