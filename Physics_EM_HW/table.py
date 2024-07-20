import numpy as np
import matplotlib.pyplot as plt
from matplotlib.table import Table

# Data sets
angles_measured_1 = np.array([0, 20, 40, 60, 80, 100, 120, 140, 160, 180])
intensity_measured_1 = np.array([5.576, 5.162, 3.528, 1.757, 0.308, 0.317, 1.520, 3.505, 4.727, 5.433])

angles_measured_2 = np.array([0, 20, 40, 60, 80, 100, 120, 140, 160, 180])
intensity_measured_2 = np.array([5.423, 5.073, 3.395, 1.307, 0.434, 0.403, 2.015, 2.583, 4.361, 5.471])

# Theoretical values from Malus's Law
I0_1 = intensity_measured_1[0]
I0_2 = intensity_measured_2[0]

theoretical_intensity_1 = I0_1 * np.cos(np.radians(angles_measured_1))**2
theoretical_intensity_2 = I0_2 * np.cos(np.radians(angles_measured_2))**2

# Calculate absolute errors
absolute_errors_1 = np.abs(intensity_measured_1 - theoretical_intensity_1)
absolute_errors_2 = np.abs(intensity_measured_2 - theoretical_intensity_2)

# Calculate uncertainties
uncertainty_1 = np.mean(absolute_errors_1) / I0_1
uncertainty_2 = np.mean(absolute_errors_2) / I0_2

# Plotting the table
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('tight')
ax.axis('off')

# Table content
table_data = [
    ["Formula for Mean Intensity", r"$\overline{I} = \frac{1}{N} \sum_{i=1}^{N} I_i$"],
    ["Mean Intensity (First Arrangement)", f"{np.mean(intensity_measured_1):.3f} W/m²"],
    ["Mean Intensity (Second Arrangement)", f"{np.mean(intensity_measured_2):.3f} W/m²"],
    ["Formula for Uncertainty", r"$\text{Uncertainty} = \frac{\text{Mean Absolute Error}}{I_0}$"],
    ["Uncertainty (First Arrangement)", f"{uncertainty_1:.3f}"],
    ["Uncertainty (Second Arrangement)", f"{uncertainty_2:.3f}"],
    ["Uncertainty in Percentage (First Arrangement)", f"{uncertainty_1 * 100:.2f}%"],
    ["Uncertainty in Percentage (Second Arrangement)", f"{uncertainty_2 * 100:.2f}%"]
]

# Create table
table = Table(ax, bbox=[0, 0, 1, 1])
n_rows = len(table_data)
n_cols = len(table_data[0])

for i in range(n_rows):
    for j in range(n_cols):
        table.add_cell(i, j, width=1/n_cols, height=1/n_rows, text=table_data[i][j], loc='center', facecolor='white')

ax.add_table(table)

plt.show()
