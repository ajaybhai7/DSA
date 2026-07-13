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

else:
    print("==== End of the program ====")


# Case1 Output
# Enter a number: 12
# Enter a Second number: 23
# The division is a/b is 0.5217391304347826
# ==== End of the program ====
# Else tabhi chalega jab try ke andar wala program sahi se run
# ho jayega


# Case2 Output
# Enter a number: skahdkha
# Please Enter a Valid input!