# Write a program to print following star pattern
# *
# **
# *** for n = 3

# Using For loop

n = int(input("Enter Number: "))
for i in range (1, n+1):
    print(i*"*")
print("End of the Program")

# Using While Loop

n = int(input("Enter Number > "))
i = 1
while i <= n:
    print(i*"*")
    i = i+1
print("End of the Program")