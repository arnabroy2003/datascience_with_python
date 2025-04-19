import matplotlib.pyplot as plt
# import numpy as np

#Line chart
# x = [1,2,3,4,5]
# y = [10,20,25,28,30]

# plt.plot(x,y, color='green', linestyle='--', marker='o')
# plt.title("Simple Line Plot")
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.grid(True)
# plt.legend(["Data Line"])
# plt.show()

#bar chart
# x = [1,2,3,4,5]
# y = [10,20,25,28,30]

# plt.bar(x,y, color='skyblue')
# plt.show()

# data = np.random.randn(1000)
# # print(data)
# plt.hist(data, bins=30, color='orange')
# plt.show()

#pie
# labels = ["Germany", "France", "Italy", "Spain"]
# sizes = [15,30,45,10]
# plt.pie(sizes, labels=labels, autopct='%1.1f%%')
# plt.title("Pie chart")
# plt.show()

#Scatter plot
# x = [5,7,8,7]
# y = [99,86,87,88]
# plt.scatter(x,y)
# plt.show()

# x = [1,2,3,4,5]
# y = [10,20,25,30,40]

# plt.subplot(1,2,1)
# plt.plot(x,y)
# plt.title("Line Plot")

# plt.subplot(1,2,2)
# plt.bar(x,y)
# plt.title("Bar chart")

# plt.tight_layout()
# # plt.show()

# plt.savefig("myplot.png")

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Month': ['Jan','Feb','Mar','Apr'],
    'Sales': [250,300,400,350]
})

df.plot(x='Month', y='Sales', kind='bar')
plt.show()