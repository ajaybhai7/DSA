# write a program to greet all the person names stored in a list "l" and whitch
# start with S.
l = ["Ajay", "Soham", "Sachin", "Rahul", "satyam"]

for name in l:
    if name.lower().startswith("s"):
        print(f"Hello {name}")

for name in l:
    if name.lower().endswith("m"):
        print(f"Hello {name}")