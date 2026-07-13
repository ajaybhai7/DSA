# Find the name whether given in a list or not!

list = ["Ajay", "Bharat", "Kunal", "Vijay", "Shahil"]

name = input("Enter your name > ")

if name in list:
    print(f"{name} You are in the list ")

else:
    print(f"{name} You are not in the list ")
