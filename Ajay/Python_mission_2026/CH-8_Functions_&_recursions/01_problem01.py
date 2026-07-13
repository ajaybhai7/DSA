# Write a program using functions to find greatest of three numbers

def greatest():
    a = int(input("Enter 1st number > ")) 
    b = int(input("Enter 2nd number > ")) 
    c = int(input("Enter 3rd number > ")) 

    if a > b and a > c:
        print("A is greatest Number")
    elif b > a and b > c:
        print("B is greatest Number")
    else:
        print("C is greatest Number")

greatest()


# In another way 

def greater(a, b, c):
    if (a > b and a > c):
        return a
    elif (b > a and b > c):
        return b
    else:
        return c

a = int(input("Enter Number A : ")) 
b = int(input("Enter Number B : ")) 
c = int(input("Enter Number C : ")) 

print(f"Greatest Number is: {greater(a, b, c)}")