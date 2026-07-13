# Write a program to greet a user with "Good Day" using function.

# def greet():
#     Name = input("Enter you'r name: ")
#     print(f"Good Day {Name}")

# greet()

# in another way

# def greet(name):
#     print("Good Day " + name)

# greet("Ajay")
# greet("Rohan")
# greet("Divya")


# Again another way with the another argument

def gooday(name, ending):
    
    print(f"Good Day {name}")
    print(ending)

gooday("Ajay", "Thank You")  # We can call this argument unlimited time where we want.
