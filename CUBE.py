import matplotlib.pyplot as plt
import numpy as np

# Generate x values
x_small = np.arange(1, 6)
x_large = np.arange(1, 5001)

# Compute cubes
cubes_small = x_small ** 3
cubes_large = x_large ** 3

# Create figure and axes
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Plot the first 5 cubic numbers
scatter1 = ax1.scatter(x_small, cubes_small, c=cubes_small, cmap='viridis', s=100, edgecolor='black')
ax1.set_title('First 5 Cubic Numbers')
ax1.set_xlabel('Number')
ax1.set_ylabel('Cube')
fig.colorbar(scatter1, ax=ax1, label='Cube Value')

# Plot the first 5000 cubic numbers
scatter2 = ax2.scatter(x_large, cubes_large, c=cubes_large, cmap='plasma', s=1)
ax2.set_title('First 5000 Cubic Numbers')
ax2.set_xlabel('Number')
ax2.set_ylabel('Cube')
fig.colorbar(scatter2, ax=ax2, label='Cube Value')

plt.tight_layout()
plt.show()
