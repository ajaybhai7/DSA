import pandas as pd


# Hamari Data 

data = {
    "Name" : ["Ajay","Saurav", "Vijay", "Rahul"],
    "Age" : [20, 23, 21, 22],
    "City" : ["Delhi", "Delhi", "Mumbai", "Pune"]
}

df = pd.DataFrame(data)

bade_log = df[df["Age"] > 20]

print("20 saal se bade log\n")
print(bade_log)

live_in_delhi = (df[ (df["Age"] > 19) & (df["City"] == "Delhi")])

print("Delhi me Rahne Wale log\n")
print(live_in_delhi)