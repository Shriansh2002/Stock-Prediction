import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the data
df = pd.read_csv('AAPL.csv') # Put your csv file here in the same directory

# Get the number of rows and columns in the data set
train_size = int(len(df) * 0.8)
train_data = df.iloc[:train_size, :]
test_data = df.iloc[train_size:, :]

# Select the feature and target variables
X_train = train_data['Open'].values.reshape(-1, 1)
y_train = train_data['Close'].values.reshape(-1, 1)
X_test = test_data['Open'].values.reshape(-1, 1)
y_test = test_data['Close'].values.reshape(-1, 1)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Calculate the root mean squared error
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print('RMSE:', rmse)

# Plot the data
plt.figure(figsize=(12, 6))
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.xlabel('Open Price ( $ )')
plt.ylabel('Close Price ( $ )')
plt.title('Apple Stock Price Prediction')
plt.show()