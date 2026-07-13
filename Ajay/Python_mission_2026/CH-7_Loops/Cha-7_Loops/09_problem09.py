# Write a Program to print following star pattern
# ***
# * *
# *** for n = 3

# Using for loop 

n = int(input("Enter Number: "))
for i in range (1, n+1):
    if i == 1 or i == n:
        print("*"*(n*2), end="")
    else:
        print("*", end="")
        print(" "* (2*n-2), end="")
        print("*", end="")
    print("")