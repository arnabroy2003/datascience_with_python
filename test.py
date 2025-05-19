import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

y_test = [1,1,0,0,0]
y_pred = [1,1,1,0,0]

y_test = np.array(y_test)
y_pred = np.array(y_pred)

print("Accuracy:", accuracy_score(y_test,y_pred))
print("Precision: ", precision_score(y_test, y_pred))
print("Recall: ",recall_score(y_test,y_pred))
print("F1 Score: ", f1_score(y_test,y_pred))

cm = confusion_matrix(y_test,y_pred)
sns.heatmap(cm, annot=True, fmt="d")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

