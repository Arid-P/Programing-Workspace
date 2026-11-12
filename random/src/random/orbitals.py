import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

# ==========================================================
# PHYSICS ENGINE: WAVEFUNCTIONS
# ==========================================================

class HydrogenOrbital:
    def __init__(self, a0=1.0):
        self.a0 = a0

    def get_psi(self, n, l, m_type, R, THETA):
        """
        Calculates the wavefunction psi for a given state.
        n: Principal quantum number
        l: Azimuthal quantum number (0 for s, 1 for p)
        m_type: "s", "px", or "py"
        """
        # Reduced distance variable
        rho = 2 * R / (n * self.a0)
        
        if l == 0:  # S-Orbitals
            if n == 1:
                radial = np.exp(-rho / 2)
            elif n == 2:
                radial = (2 - rho) * np.exp(-rho / 2)
            elif n == 3:
                radial = (27 - 18 * rho + 2 * rho**2) * np.exp(-rho / 2)
            return radial
            
        elif l == 1:  # P-Orbitals
            if n == 2:
                radial = rho * np.exp(-rho / 2)
            elif n == 3:
                radial = rho * (6 - rho) * np.exp(-rho / 2)
            
            # Angular component
            if m_type == "px":
                angular = np.cos(THETA)
            else:  # py
                angular = np.sin(THETA)
                
            return radial * angular
            
        return np.zeros_like(R)

# ==========================================================
# VISUALIZATION LOGIC
# ==========================================================

def plot_orbital(orbital_name="3s", grid_res=800):
    """
    Generates and plots the probability density.
    Using LogNorm is the secret to seeing radial nodes!
    """
    # 1. Setup Parameters
    n = int(orbital_name[0])
    l = 0 if "s" in orbital_name else 1
    m_type = orbital_name[1:] # "s", "px", or "py"
    
    # Scale the viewing window based on n
    # Orbitals get significantly larger as n increases
    limit = n * n * 2.2 
    
    # 2. Create Coordinate System
    x = np.linspace(-limit, limit, grid_res)
    y = np.linspace(-limit, limit, grid_res)
    X, Y = np.meshgrid(x, y)
    
    # Convert to polar coordinates for the math
    R = np.sqrt(X**2 + Y**2) + 1e-15 # Avoid div by zero
    THETA = np.arctan2(Y, X)
    
    # 3. Calculate Wavefunction and Probability Density
    engine = HydrogenOrbital()
    psi = engine.get_psi(n, l, m_type, R, THETA)
    prob_density = np.abs(psi)**2
    
    # 4. Create Plot
    fig, ax = plt.subplots(figsize=(10, 10), facecolor='black')
    ax.set_facecolor('black')
    
    # We use LogNorm to handle the extreme range of values.
    # vmin ensures we don't try to log(0), and sets the background 'floor'.
    norm = LogNorm(vmin=prob_density.max() * 1e-5, vmax=prob_density.max())
    
    im = ax.imshow(
        prob_density,
        extent=[-limit, limit, -limit, limit],
        origin='lower',
        cmap='magma', # 'magma' or 'inferno' provide high contrast for nodes
        norm=norm,
        interpolation='bilinear'
    )
    
    # 5. Aesthetics
    title_str = f"Hydrogen {orbital_name.upper()} Orbital\n$|\psi|^2$ Probability Density (Log Scale)"
    ax.set_title(title_str, color='white', fontsize=16, pad=20)
    ax.set_xlabel("x ($a_0$)", color='white', fontsize=12)
    ax.set_ylabel("y ($a_0$)", color='white', fontsize=12)
    
    ax.tick_params(colors='white', which='both')
    for spine in ax.spines.values():
        spine.set_edgecolor('#444444')
    
    # Add a small white dot for the nucleus
    ax.scatter(0, 0, color='white', s=10, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# ==========================================================
# RUN
# ==========================================================

if __name__ == "__main__":
    # OPTIONS: "1s", "2s", "3s", "2px", "2py", "3px", "3py"
    plot_orbital("3s")