import pandas as pd

data = {
    "Product": ["Coconut oil","Biscuit","Coconut oil","Biscuit"],
    "Area": ["East","West","East","East"],
    "Sales": [100,150,200,100]
}

df = pd.DataFrame(data)

pivot = pd.pivot_table(df, values='Sales', index='Product', columns='Area', aggfunc='sum')

print(pivot)

# create a csv file with column Class, Subject, Marks