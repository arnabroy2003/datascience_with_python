from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

X = [
    [4.2, 22], [4.4, 25], [4.6, 28], [4.7, 32], [4.9, 36], [5.0, 38], [5.1, 40],
    [5.3, 44], [5.5, 60], [5.6, 65], [5.7, 67], [5.8, 70], [5.9, 75],
    [6.0, 78], [6.1, 80], [6.2, 85], [6.3, 88], [6.4, 90]
]

y = [
    0, 0, 0, 0, 0, 0, 0,     
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
]

# x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

model = SVC(kernel='linear')
scores = cross_val_score(model, X,y,cv=5)
print("Scores for Each fold: ",scores)
print("Average Accuracy: ", scores.mean()*100,"%")
# model.fit(x_train,y_train)

# y_pred = model.predict(x_test)
# accuracy = accuracy_score(y_test, y_pred)


