# sigmoid Function: sigmoid(z) = 1/ (1 + e^(-z))

# if Probability > 0.5 -> class 1 (yes)
# if ""         < 0.5 -> class 0 (no)

#1. Spam Detection (Spam/Not Spam)
#2. Loan Approval (Approved/Rejected)
#3. Dsease Prediction (Has Disease/No Disease)

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score

df = pd.read_csv("study.csv")

x = df[['Hours_Studied']]
y = df['Passed']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("Prediction: ",y_pred)
print("Actual: ", y_test.values)

print("Accuracy: ", accuracy_score(y_test,y_pred))
print("Precision: ", precision_score(y_test, y_pred))
