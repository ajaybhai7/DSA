# Write a program to print multiplication table using for loop in reverse
# order

n = int(input("Enter Number > "))

for i in range (1, 11):
    tp = n*(11-i)
    print(f"{n} x {(11-i)} = {tp}")

