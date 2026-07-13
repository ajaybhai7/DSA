try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a Second number: "))

    if b == 0 or a == 0:
        raise ZeroDivisionError("Hey our program is not " \
        "meant to devide number by zero")
    else:
        print(f"The division is a/b is {a/b}")
except ValueError:
    print("Please Enter a Valid input!")
