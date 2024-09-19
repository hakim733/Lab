import matplotlib.pyplot as plt
import numpy as np
from scipy import stats  # For trimmed mean

# Data 
Smokers = [69.3, 56.0, 22.1, 53.2, 48.1, 52.7, 60.2, 43.8, 23.2, 47.6, 34.4, 13.8]
Non_smokers = [28.6, 25.1, 26.4, 29.8, 28.4, 38.5, 30.6, 31.8, 41.6, 36.0, 37.9, 13.9, 34.9, 30.2, 21.1]

# For the Smokers group
mean_smokers = np.mean(Smokers)
median_smokers = np.median(Smokers)
trimmed_mean_smokers = stats.trim_mean(Smokers, proportiontocut=0.1)
sdv_smokers = np.std(Smokers)

# Print out the calculated statistics for Smokers
print("Smokers mean is =", mean_smokers)
print("Smokers group median is =", median_smokers)
print("Smokers group 10% Trimmed Mean:", trimmed_mean_smokers)
print("Smokers standard deviation:", sdv_smokers)

# For the Non-smokers group
mean_non_smokers = np.mean(Non_smokers)
median_non_smokers = np.median(Non_smokers)
trimmed_mean_non_smokers = stats.trim_mean(Non_smokers, proportiontocut=0.1)
sdv_non_smokers = np.std(Non_smokers)

# Print out the calculated statistics for Non-smokers
print("Non-smokers mean is =", mean_non_smokers)
print("Non-smokers group median is =", median_non_smokers)
print("Non-smokers group 10% Trimmed Mean:", trimmed_mean_non_smokers)
print("Non-smokers standard deviation:", sdv_non_smokers)

# Create the plot
plt.figure(figsize=(12, 2))  # Adjust the height to make it look like a 1D plot

# Plot the Smokers and Non-smokers data as dots along the X-axis
plt.plot(Smokers, np.ones_like(Smokers), 'ro', markersize=10, label='Smokers')  # 'ro' for red dots
plt.plot(Non_smokers, np.ones_like(Non_smokers), 'bo', markersize=10, label='Non-smokers')  # 'bo' for blue dots

# Add labels and title
plt.yticks([])  # Hide Y-axis
plt.gca().get_yaxis().set_visible(False)  # Another way to ensure Y-axis is hidden
plt.xlabel('Values')
plt.title("Unidimensional Dot Plot of Smokers and Non-smokers", fontsize=16)
plt.legend()

# Show the plot
plt.show()
