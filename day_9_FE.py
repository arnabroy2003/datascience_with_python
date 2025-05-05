#Encoding
#Categorical Gender -> Male(0), Female(1), Third-gen(2)
# from sklearn.preprocessing import LabelEncoder
# le = LabelEncoder()
# # gender = ["Male","Female","Female","Male","Female"]
# colors = ['Red','Green','Red','Blue','Green','Blue','Blue','Red']
# encoded = le.fit_transform(colors)
# print(encoded)

# import pandas as pd
# data = {
#     'color': ['Red','Green','Blue']
# }
# df = pd.DataFrame(data)
# one_hot = pd.get_dummies(df['color'])
# print(one_hot)

#Scaling
# from sklearn.preprocessing import StandardScaler

# data = [[2],[6],[3],[5],[4]]
# scaler = StandardScaler()

# scaled_data = scaler.fit_transform(data)
# print(scaled_data)

#Feature Selection
import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2

data = {
    'Age': [22,25,47,52,46],
    'Salary': [15000,29000,48000,60000,52000],
    'own_house': [0,1,1,1,0],
    'Buys_Insurance': [0,0,1,1,1]
}

df = pd.DataFrame(data)

x = df[['Age','Salary','own_house']]
y = df['Buys_Insurance']

selector = SelectKBest(score_func=chi2, k=2)
new_x = selector.fit_transform(x, y)

mask = selector.get_support()
seleced_features = x.columns[mask]

print("Selected Features: ",list(seleced_features))