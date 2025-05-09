# from sklearn.linear_model import LinearRegression

# x = [[8],[10],[12]]
# y = [10,13,16]

# model = LinearRegression()
# model.fit(x,y)

# new_x = 20
# predict_y = model.predict([[new_x]])
# print(f"Expected Price will be ${predict_y}")

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd

data = {
    "Size (sqft)": [850, 900, 1200, 1500, 1800],
    "Bedrooms": [2, 3, 3, 4, 4],
    "Location Index": [1, 2, 3, 3, 4],
    "Price ($)": [200000, 220000, 280000, 350000, 400000]
}

df = pd.DataFrame(data)

x = df[["Size (sqft)" , "Bedrooms" , "Location Index"]]
y = df["Price ($)"]

x_train, x_test, y_train, y_test = train_test_split(x , y ,test_size=0.2,random_state=42)
# print("Training Features: \n", x_train)
# print("\nTest Features: \n", x_test)
# print("\nTraining Labels: \n", y_train)
# print("\nTest Labels: \n", y_test)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

model = LinearRegression()
model.fit(x_train_scaled, y_train)
print("Model Trained Successfully")

y_pred = model.predict(x_test_scaled)
print("With Scale: ")
print(f"Predict price {y_pred}")
print(f"Actual price {y_test.values}")

model1 = LinearRegression()
model1.fit(x_train, y_train)

y_pred1 = model1.predict(x_test)
print("Without Scale: ")
print(f"Predict price {y_pred1}")
print(f"Actual price {y_test.values}")
