# Write a function to take input from the user and squre the number

def get_squre(number):

    square = number * number
    return square

number = int(input("Enter a number: "))

squre = get_squre(number)
print(f"The Squre is : {squre}")