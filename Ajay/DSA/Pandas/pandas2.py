import pandas as pd

data = {
    "Name" : ["Ajay", "Vijay", "Rahul"],
    "Age" : [20, 21, 22],
    "City" : ["Delhi", "Mumbai", "Pune"]
}

df = pd.DataFrame(data) # Data frame table banaya 
print(df) # Table Print Karaya 

print(f'''
------- Sabka Name --------
{df["Name"]}

--------- Sabka Age ------
{df["Age"]}

-------- Sabka City ------
{df["City"]}


-------- Sabse bada Kaun ? ---------

{df["Age"].max()}

------ Average Age of Class --------

{df["Age"].mean()}
''')

