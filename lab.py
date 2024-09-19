import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  # For strip plot
from scipy import stats  # For trimmed mean

# Data array
Array1 = [18.71, 21.41, 20.72, 21.81, 19.29, 22.43, 20.17, 23.71, 19.44, 20.50, 
          18.92, 20.33, 23.00, 22.85, 19.25, 21.77, 22.11, 19.77, 18.04, 21.12]

# Calculate statistics
Mean = np.mean(Array1)
Median = np.median(Array1)
trimmed_mean = stats.trim_mean(Array1, proportiontocut=0.1)

# Print out the calculated statistics
print("The mean is =", Mean)
print("The median is =", Median)
print("10% Trimmed Mean:", trimmed_mean)

# Create the plot
plt.figure(figsize=(10, 2))  # Adjust the height to make it look like a 1D plot

# Plot the data as dots along the X-axis
plt.plot(Array1, np.ones_like(Array1), 'bo', markersize=10)  # 'bo' for blue dots

# Remove Y-axis
plt.yticks([])  # Hide Y-axis
plt.gca().get_yaxis().set_visible(False)  # Another way to ensure Y-axis is hidden

# Add a title
plt.title("Unidimensional Dot Plot", fontsize=16)

# Show the plot
plt.show()
print("test")