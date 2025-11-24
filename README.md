**psoriasis-cytokine-model**
### **Nonlinear ODE Model of IL-36 / IL-17 Cytokine Interaction and Bistability Dynamics in Psoriasis**  
*(Master’s Thesis, 2025)*

---

**Overview**
This repository contains a computational **dynamical systems model** that describes the regulatory interaction between **IL-36 and IL-17 cytokines**, which play a crucial role in psoriasis inflammation. The objective of this project is to explore how **nonlinear feedback**, **saturation dynamics**, and **parameter-dependent regulation** can lead to **bistability** and **switch-like transitions** in inflammatory signalling.

---

**Model Description**
The system is formulated using two coupled **ordinary differential equations (ODEs)** representing the temporal evolution of IL-36 and IL-17 concentrations. The model incorporates:

- **Positive feedback regulation**
- **Saturating nonlinear response terms**
- **Natural production and degradation rates**
- **Parameter-dependent shifts in stability**


---

**Methods & Analysis**
The project implements several computational methods, including:

- **Numerical integration** of nonlinear ODE systems
- **Bifurcation-style and stability analysis**
- **Time-series simulations** of cytokine dynamics
- **Phase-plane visualisation**
- **Parameter sensitivity exploration** to map regions supporting bistability

---

**Technologies & Libraries Used**

**Python**
- `NumPy` — numerical computation  
- `SciPy` — differential equation solvers and mathematical utilities  
- `Matplotlib` — visualisation of time-series and phase-plane dynamics  
- `Pandas` — parameter management and structured data  
- `SymPy` — symbolic mathematics for steady-state and Jacobian analysis  
- `Jupyter Notebook` — reproducible analysis environment  
- **Python 3.7 / BaseEnvironment / virtual environments**

**MATLAB**
- Nonlinear dynamics simulation using **`ode45`**, **`ode15s`**
- Time-series trajectories and stability analysis
- Phase-plane plotting and equilibrium interpretation

---
