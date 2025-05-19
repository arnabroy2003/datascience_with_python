import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# Load dataset
df = pd.read_csv("Play.csv")

print(df['Weather'])

# Initialize separate encoders
# le_weather = LabelEncoder()
# le_temp = LabelEncoder()
# le_play = LabelEncoder()

# # Apply encoding using correct encoders
# df['Weather'] = le_weather.fit_transform(df['Weather'])      # encodes Sunny, Overcast, Rainy
# df['Temp'] = le_temp.fit_transform(df['Temp'])               # encodes Hot, Mild, Cool
# df['Playoutside'] = le_play.fit_transform(df['Playoutside']) # encodes No, Yes

# # Prepare features and label
# x = df[['Weather','Temp']]
# y = df['Playoutside']

# # Train model
# model = DecisionTreeClassifier()
# model.fit(x, y)

# # Predict
# weather = le_weather.transform(['Overcast'])  # now works correctly
# temp = le_temp.transform(['Mild'])

# prediction = model.predict([[weather[0], temp[0]]])
# decoded = le_play.inverse_transform(prediction)[0]

# print(decoded)
