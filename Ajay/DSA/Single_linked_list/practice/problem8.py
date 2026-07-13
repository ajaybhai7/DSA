# Making a calculator function to calculate two numbers

def calculator():
    num1 = int(input("Enter your first number: "))
    operator = input("Enter (x,/,-,+): ")
    num2 = int(input("Enter 2nd Number: "))

    if operator == "x":
        print(f"{num1} x {num2} = {num1 * num2}")
    
    elif operator == "/":
        print(f"{num1} / {num2} = {num1 // num2}")

    elif operator == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    
    elif operator == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    
    else:
        print("Enter the Correct operator or Number")
    

calculator()