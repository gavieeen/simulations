import numpy as np
import matplotlib.pyplot as plt

# Data
angles_measured = np.array([0, 20, 40, 60, 80, 100, 120, 140, 160, 180])
intensity_measured = np.array([5.576, 5.162, 3.528, 1.757, 0.308, 0.317, 1.520, 3.505, 4.727, 5.433])

# Calculate the mean and standard deviation
mean_intensity = np.mean(intensity_measured)
std_intensity = np.std(intensity_measured)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(angles_measured, intensity_measured, color='blue', label='Measured Data')
plt.errorbar(angles_measured, intensity_measured, yerr=std_intensity, fmt='o', color='red', label='Uncertainty')
plt.xlabel('Angle (degrees)')
plt.ylabel('Intensity (W/m^2)')
plt.title('Light Intensity vs Angle with Uncertainty')
plt.legend()
plt.grid(True)
plt.show()

# Print the results
print(f"Mean Intensity: {mean_intensity:.3f} W/m^2")
print(f"Standard Deviation of Intensity (Uncertainty): {std_intensity:.3f} W/m^2")
