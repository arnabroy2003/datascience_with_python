from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import pickle

emails = [
    "Win a brand new car now",              # spam
    "Meeting scheduled at 10 AM",           # not spam
    "Congratulations! You won a prize",     # spam
    "Lunch at 1 PM?",                       # not spam
    "Get cheap meds without prescription",  # spam
    "Can we reschedule our call?",          # not spam
    "Earn $1000 per day from home",         # spam
    "Please find the attached report",      # not spam
    "Limited time offer, act now",          # spam
    "Team meeting rescheduled to Friday"    # not spam
]

labels = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0] #1 = spam, 0 = Not spam

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

x_train, x_test, y_train, y_test = train_test_split(X,labels, test_size=0.2, random_state=42)

Model = SVC(kernel='linear')
Model.fit(x_train,y_train)

with open("model.pkl","wb") as f:
    pickle.dump(Model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Model Saved")

# y_pred = Model.predict(x_test)

# print(f"Accuracy:{accuracy_score(y_test,y_pred)*100}%")

# scores = cross_val_score(Model, X,labels,cv=5)
# print("Average Accuracy with cross fold: ", scores.mean()*100,"%")

# new_email = ["Get your free iPhone now"]
# new_vector = vectorizer.transform(new_email)
# prediction = Model.predict(new_vector)
# if prediction[0] == 1:
#     print("Spam")
# else:
#     print("Not Spam")

