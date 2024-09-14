import numpy as np
import pandas as pd
# Create a Pandas DataFrame from a NumPy array
data = np.array([[0.5, 2.0, 3.0], [4.0, 5.0, np.nan], [7.0, 8.0, 9.0]])
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
# Impute missing values using NumPy
df.fillna(df.mean(), inplace=True)
# Scale the data using NumPy
df_scaled = (df - df.mean()) / df.std()

# Load data and show the top 5 rows
df = pd.read_csv('house_prices.csv')
print(df.head())
# Create X and y arrays
X = df['sqft'].values.reshape(-1, 1)
y = df['price'].values.reshape(-1, 1)
# Compute regression coefficients
beta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
# Print coefficients
print('Coefficients: ', beta)
