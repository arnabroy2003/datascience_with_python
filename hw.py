import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
# print(df.head())

# sns.histplot(df["total_bill"])
# plt.show()

sns.boxplot(x='day', y='total_bill', data=df)
plt.title("Boxplot by Day")
plt.show()