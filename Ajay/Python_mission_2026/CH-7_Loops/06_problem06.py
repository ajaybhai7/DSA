# Write a program to find a factorial of n number using loops

n = int(input("Enter Number > "))
i = 1
factorial = 1

while i <= n:
    factorial *= i
    i +=1
print(f"factorial of {n} : {factorial}")


# Using For loop

n = int(input("Enter Number > "))
factorial = 1
for i in range (1, n+1):
    factorial *=i
print(f"factorial of {n} : {factorial}")

