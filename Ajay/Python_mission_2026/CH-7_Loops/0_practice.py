# Write a Program to print star pattern,
#   *
#  ***
# *****

# n = int(input("Enter Number: "))
# for i in range (1, n+1):
#     print(" "* (n-i), end="")
#     print("*"* (2*i-1))


# Using While Loop

n = int(input("Enter Number: "))
i = 1
while i <= n:
    print(" "* (n-i), end="")
    print("*"* (2*i-1))
    i = i+1
