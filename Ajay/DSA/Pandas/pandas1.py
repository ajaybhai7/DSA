import pandas as pd


# Hamari Data 

data = {
    "Name" : ["Ajay", "Vijay", "Rahul"],
    "Age" : [20, 21, 22],
    "City" : ["Delhi", "Mumbai", "Pune"]
}

df = pd.DataFrame(data) # Data frame table banaya 
print(df) # Table Print Karaya 


excel = df.to_csv("Pandas.csv", index=False)
print(excel)
