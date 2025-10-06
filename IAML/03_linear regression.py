# Step 1 : import library
import pandas as pd

# Step 2 : import data
salary = pd.read_csv('https://github.com/ybifoundation/Dataset/raw/main/Salary%20Data.csv')

# Step 3 : define target (y) and features (X)
y = salary['Salary']
X = salary[['Experience Years']]

# Step 4 : train test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=2529)

# Step 5 : select model
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# Step 6 : train or fit model
model.fit(X_train, y_train)

# Step 7 : predict model
y_pred = model.predict(X_test)

# Step 8 : model accuracy
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error, r2_score

mae = mean_absolute_error(y_test, y_pred)
mape = mean_absolute_percentage_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

# Adjusted R2
def adjusted_r2(r2, n, k):
    return 1 - (1 - r2) * (n - 1) / (n - k - 1)

adj_r2 = adjusted_r2(r2, X_test.shape[0], X_test.shape[1])

# Print metrics
print("MAE: ", mae)
print("MAPE: ", mape)
print("MSE: ", mse)
print("RMSE: ", rmse)
print("R2 Score: ", r2)
print("Adjusted R2 Score: ", adj_r2)

# Step 9 : visualize model
import matplotlib.pyplot as plt

plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted')
plt.xlabel('Experience Years')
plt.ylabel('Salary')
plt.title(f'Experience Years vs Salary\nR2 = {r2:.3f}, Adjusted R2 = {adj_r2:.3f}')
plt.legend()
plt.show()
