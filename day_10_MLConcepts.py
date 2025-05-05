# Ml formula - Input(Fretures) -> Algorithm -> Output(Prediction)
'''
Machine Learning is a method of teaching computers to learn patterns from data
and make prediction or decisions without being explicitly promrammed.

Type Of Learning:
1. Supervised Learning
2. Unsupervised Learning
3. Semi-Supervised / Reinforcement Learning
'''

'''
Supervised Learning (learn from teacher):
1. cat image (this is cat) /labelled
2. dog image (this is dog) /labelled
Example: Email spam detection
common Algo: Linear Regression, SVM, etc

Unsupervised Learning (learn itself):
Many Friuts images ->
create groups itself
1. group for all rounded red fruit (apple)
2. group for all yellow long fruit (banana)
Example: Customer Segmentation
common Algo: K-means, PCA, etc
'''

# Train-Test Split
import pandas as pd
from sklearn.model_selection import train_test_split
data = {
    'Age': [25,30,45,35,23,40,60,48,33,50],
    'Salary': [40000,50000,80000,60000,42000,75000,100000,85000,62000,90000],
    'Purchased': [0,1,1,1,1,0,1,1,0,1] # 0 = no, 1 = yes
}

df = pd.DataFrame(data)

x = df[['Age','Salary']]
y = df['Purchased']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

print("Training Features: \n", x_train)
print("\nTest Features: \n", x_test)
print("\nTraining Labels: \n", y_train)
print("\nTest Labels: \n", y_test)



