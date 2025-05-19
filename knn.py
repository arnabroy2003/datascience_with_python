from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_csv("movie.csv")

x = df[['Duration']]
y = df['Genre']

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x, y_encoded)

new_duration = [[130]]
pred = knn.predict(new_duration)
predicted_genre = label_encoder.inverse_transform(pred)
print(predicted_genre)