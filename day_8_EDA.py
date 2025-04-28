import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('students.csv')

# print(df.shape)
# print(df.dtypes)

# print(df.describe())

# print(df.isnull().sum())

# print(df["Age"].unique())
# print(df["Age"].value_counts())

# Q1 = df["Maths"].quantile(0.25)
# Q3 = df["Maths"].quantile(0.75)

# IQR = Q3 - Q1

# lower_limit = Q1 - 1.5 * IQR
# upper_limit = Q3 + 1.5 * IQR

# outliers = df[(df['Maths'] < lower_limit) | df['Maths'] > upper_limit]
# print(outliers)

# sns.boxplot(x=df['Maths'])
# plt.show()