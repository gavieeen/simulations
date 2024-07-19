import numpy as np
import matplotlib.pyplot as plt

# Data
angles_measured = np.array([0, 20, 40, 60, 80, 100, 120, 140, 160, 180])
intensity_measured = np.array([5.576, 5.162, 3.528, 1.757, 0.308, 0.317, 1.520, 3.505, 4.727, 5.433])

# Malus's law function
I0 = intensity_measured[0]
angles_smooth = np.linspace(0, 180, 500) # continous angles
intensity_malus_smooth = I0 * np.cos(np.radians(angles_smooth))**2

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(angles_measured, intensity_measured, color='blue', label='Measured Intensity')
plt.plot(angles_smooth, intensity_malus_smooth, color='red', linestyle='-', label="Malus's Law")

# Vertical differences shown as dashed lines
for i, angle in enumerate(angles_measured):
    intensity_malus_at_angle = I0 * np.cos(np.radians(angle))**2
    plt.plot([angle, angle], [intensity_measured[i], intensity_malus_at_angle], 'k--')
    plt.text(angle, (intensity_measured[i] + intensity_malus_at_angle) / 2, f'{abs(intensity_measured[i] - intensity_malus_at_angle):.2f}',
             ha='right', va='bottom' if intensity_measured[i] > intensity_malus_at_angle else 'top', color='black')

# Labels and legend
plt.xlabel('Angle (degrees)')
plt.ylabel('Intensity (W/m^2)')
plt.title('Measured Intensity vs Malus\'s Law')
plt.legend()
plt.grid(True)

# Show plot
plt.show()
