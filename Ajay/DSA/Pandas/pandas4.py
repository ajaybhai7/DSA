import pandas as pd


data = {
    "Name" : ["Ajay","Saurav", "Vijay", "Rahul"],
    "Age" : [20, 23, 21, 22],
    "City" : ["Delhi", "Delhi", "Mumbai", "Pune"],
    "Epl" : [12, 34, 21, 11]
}

df = pd.DataFrame(data)

df["Age_in_Months"] = df["Age"]*12

sorted_df = df.sort_values(by="Name")
print("\n",sorted_df)

epl_sort = df.sort_values(by="Epl")
print("\n",epl_sort)

age_sort = df.sort_values(by="Age")
print("\n",age_sort)

d_epl_s = df.sort_values(by="Epl", ascending = False)
print(f"\n{d_epl_s}")