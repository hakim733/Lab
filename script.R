# Data: Length of life in years of 30 fuel pumps
data <- c(2.0, 3.0, 0.3, 3.3, 1.3, 0.4, 0.2, 6.0, 5.5, 6.5, 0.2, 2.3, 1.5, 4.0, 5.9, 1.8, 4.7, 0.7, 4.5, 0.3, 1.5, 0.5, 2.5, 5.0, 1.0, 6.0, 5.6, 6.0, 1.2, 0.2)

# Define class intervals (bins)
bins <- seq(0, 7, by = 1)

# Compute the frequency distribution
frequency <- hist(data, breaks = bins, plot = FALSE)$counts

# Compute the relative frequencies
relative_frequency <- frequency / length(data)

# Combine class intervals, frequencies, and relative frequencies into a data frame
class_intervals <- paste(bins[-length(bins)], "-", bins[-1], sep = "")
result <- data.frame(Class = class_intervals, Frequency = frequency, Relative_Frequency = relative_frequency)

# Print the result
print(result)

# Data: Length of life in years of 30 fuel pumps
data <- c(2.0, 3.0, 0.3, 3.3, 1.3, 0.4, 0.2, 6.0, 5.5, 6.5, 0.2, 2.3, 1.5, 4.0, 5.9, 1.8, 4.7, 0.7, 4.5, 0.3, 
          1.5, 0.5, 2.5, 5.0, 1.0, 6.0, 5.6, 6.0, 1.2, 0.2)

# 1. Sample Mean
sample_mean <- mean(data)

# 2. Sample Range
sample_range <- range(data)  # This returns the min and max values
range_value <- diff(sample_range)  # Compute the range by subtracting min from max

# 3. Sample Standard Deviation
sample_sd <- sd(data)

# Display the results
cat("Sample Mean:", sample_mean, "\n")
cat("Sample Range:", range_value, "\n")
cat("Sample Standard Deviation:", sample_sd, "\n")



