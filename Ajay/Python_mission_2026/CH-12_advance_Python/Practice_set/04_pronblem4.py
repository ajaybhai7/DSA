# Write a program to display a/b where a and b are integers. if b = 0 
# Display infinite by handling the "ZeroDivisonError".
try:
    a = int(input("Enter a Number: "))
    b = int(input("Enter 2nd Number: "))
    if a == 0 or b == 0:
        ZeroDivisionError
        print("Infinite")

    else:

        print(f"The Division of {a}/{b} is {a/b}")

except ValueError:
    print("Enter a valid number")


# We can also do it simple form but not a error handler 

try:
    a = int(input("Enter a Number: "))
    b = int(input("Enter 2nd Number: "))
    print(f"The Division of {a}/{b} is {a/b}")
except ZeroDivisionError as v:
    print("Infinite")
    

# Output
# p1
# Enter a Number: 12
# Enter 2nd Number: 0
# Infinite
# p2
# Enter a Number: 21
# Enter 2nd Number: 0
# Infinite