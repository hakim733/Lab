from scipy import stats
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
Array1=[18.71, 21.41, 20.72, 21.81, 19.29, 22.43, 20.17, 23.71, 19.44, 20.50, 18.92, 20.33, 23.00, 22.85, 19.25, 21.77, 22.11, 19.77, 18.04, 21.12]
Mean= np.mean(Array1)
print("the mean is =",Mean)
Median=np.median(Array1)
print("the median is =", Median)
print(sp.__version__)
stats.trim_mean(Array1, 0.1)
# Compute 10% trimmed mean
trimmed_mean = stats.trim_mean(Array1, proportiontocut=0.1)
print("10% Trimmed Mean:", trimmed_mean)
#plotting the data
plt(Array1)

