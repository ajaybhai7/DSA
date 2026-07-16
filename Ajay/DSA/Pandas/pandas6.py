import pandas as pd

data = {
    "Name" : ["Ajay", "Amit", "Rohan", "Vijay", "Rahul", "Priya"],
    "Age"  : [20, 25, 23, 21, 19, 22],
    "City" : ["Delhi", "Mumbai", "Delhi", "Mumbai", "Pune", "Pune"]
}

df = pd.DataFrame(data)

city_age = df.groupby("City")["Age"].mean()
print(city_age)

df.to_csv("Pandas_Data.csv", index = False)
