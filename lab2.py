import matplotlib.pyplot as plt
import numpy as np
from scipy import stats  # For trimmed mean


# Data for control and treatment groups
control_group = [7, 3, -4, 5, 22, -7, 14, 2, 9, 5]
treatment_group = [-6, 5, 9, 12, 4, 4, 37, 5, 3, 3]

# Create dot plot
plt.figure(figsize=(10, 6))

# Plot control group
plt.plot(control_group, [1] * len(control_group), 'bo', label='Control Group')

# Plot treatment group
plt.plot(treatment_group, [2] * len(treatment_group), 'ro', label='Treatment Group')

# Labels and formatting
plt.yticks([1, 2], ['Control Group', 'Treatment Group'])
plt.title('Dot Plot of Control and Treatment Groups')
plt.xlabel('Value')
plt.grid(True, axis='x', linestyle='--', alpha=0.7)
plt.legend()
# Show plot
plt.show()


