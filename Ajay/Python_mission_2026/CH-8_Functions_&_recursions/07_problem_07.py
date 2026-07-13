# write a python function to print multiplication table of given number.

# def multiply(n):
#     for i in range (1,11):
#         print(f"{n} x {i} = {n*i}")
# n = int(input("Enter Number: "))
# multiply(n)

# 
def multy(n, i=1):
    if i > 10:
        return
    print(f"{n} x {i} = {n*i}")
    multy(n, i+1)
n = int(input("Enter Number > "))
multy(n)

