import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVC

# Dataset
X = [
    [4.5, 30],  # Child
    [4.7, 35],  # Child
    [5.0, 40],  # Child
    [5.5, 60],  # Adult
    [5.8, 70],  # Adult
    [6.0, 80]   # Adult
]
y = [0, 0, 0, 1, 1, 1]  # 0 = Child, 1 = Adult

# Train SVM model
model = SVC(kernel='linear')
model.fit(X, y)

# New data point
new_data = [[4.2, 37]]
prediction = model.predict(new_data)

# Predict class and print
if prediction[0] == 0:
    print("Child")
else:
    print("Adult")

# Convert to numpy for plotting
X_np = np.array(X)
y_np = np.array(y)

# Plot data points
plt.figure(figsize=(8, 6))
plt.scatter(X_np[y_np == 0][:, 0], X_np[y_np == 0][:, 1], color='blue', label='Child')
plt.scatter(X_np[y_np == 1][:, 0], X_np[y_np == 1][:, 1], color='green', label='Adult')

# Plot the new data point
plt.scatter(new_data[0][0], new_data[0][1], color='red', label='New Data', marker='x', s=100)

# Plot decision boundary
w = model.coef_[0]
b = model.intercept_[0]

# Equation of line: w1*x1 + w2*x2 + b = 0 -> x2 = -(w1*x1 + b)/w2
x_vals = np.linspace(4, 6.5, 100)
y_vals = -(w[0] * x_vals + b) / w[1]
plt.plot(x_vals, y_vals, 'k--', label='Decision Boundary')

plt.xlabel("Height (feet)")
plt.ylabel("Weight (kg)")
plt.title("SVM Classification (Child vs Adult)")
plt.legend()
plt.grid(True)
plt.show()
