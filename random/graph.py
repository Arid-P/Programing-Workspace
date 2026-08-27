import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Realistic experimental points
time_pts = np.array([0, 120, 240, 360, 480, 600, 720, 840, 960, 1080, 1200, 1320])
temp_pts = np.array([95, 86, 80, 80, 80, 80, 68, 58, 50, 44, 39, 35])

# Create smooth curve segments for realistic rendering
# 1. Liquid cooling (0 to 240s)
t_liquid = np.linspace(0, 240, 100)
spline_liq = make_interp_spline(time_pts[:3], temp_pts[:3], k=2)
T_liquid = spline_liq(t_liquid)

# 2. Phase change plateau (240 to 600s)
t_plateau = np.linspace(240, 600, 50)
T_plateau = np.full_like(t_plateau, 80.0)

# 3. Solid cooling curve (600 to 1320s)
t_solid = np.linspace(600, 1320, 200)
spline_sol = make_interp_spline(time_pts[5:], temp_pts[5:], k=2)
T_solid = spline_sol(t_solid)

# Concatenate smooth curve
t_smooth = np.concatenate([t_liquid, t_plateau, t_solid])
T_smooth = np.concatenate([T_liquid, T_plateau, T_solid])

# Plot setup
plt.figure(figsize=(10, 6))

# Smooth authentic cooling curve
plt.plot(t_smooth, T_smooth, color='navy', linewidth=2.5, label='Cooling Curve')

# Discrete observation points
plt.scatter(time_pts, temp_pts, color='blue', s=45, zorder=5, label='Observations')

# Markings required by the manual
plt.axhline(y=80, color='red', linestyle='--', linewidth=1.5, label='Melting Point (80°C)')
plt.axhline(y=26, color='green', linestyle='--', linewidth=1.5, label='Room Temperature (26°C)')

# Annotations for file tracing
plt.text(380, 82, 'Change of State\n(Temperature Constant)', color='darkred', fontsize=10, fontweight='semibold')
plt.text(850, 28, 'Room Temp = 26°C', color='darkgreen', fontsize=10)

# Labels and Styling
plt.title('Cooling Curve of Molten Wax', fontsize=14, fontweight='bold')
plt.xlabel('Time (s)', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.ylim(20, 105)
plt.xlim(-30, 1400)
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.legend(loc='upper right')

plt.show()
