# Write a function to print True or False When the number is even or not

def is_even(number):

    if number % 2 == 0:
        return True
    
    else:
        return False
    
number = int(input("Enter a Number :"))
iseven = is_even(number)

print(f"The Number is Given {iseven}")