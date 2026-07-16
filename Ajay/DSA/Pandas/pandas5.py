import pandas as pd

data = {
    "Name" : ["Ajay", "Amit", "Rohan", None, "Rahul"],
    "Age"  : [20, None, 23, 21, 19],
    "City" : ["Delhi", "Rajsthan", "Haryana", "UP", None]
}

df = pd.DataFrame(data)
filtered_df = df.fillna(0)
rm_row_df = df.dropna()

print(f'''
------- Normal Data Sheet -------

{df}

------- Filter Data Sheet -------

{filtered_df}

------- Removed Filtered Data -------

{rm_row_df}
''')