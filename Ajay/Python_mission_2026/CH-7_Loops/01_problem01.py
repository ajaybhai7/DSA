#  Write a program to print multiplication table using for loop

# table_number = int(input("Enter a number to print multiplication Table > "))
# i = 1

# while i <= 10:
#     mul = i*table_number
#     print(f"{i} x {table_number} = {mul}")
#     i +=1

# print("===Done===")


# Using for loop

table_number = int(input("Enter number to print a Table > "))
for i in range(1, 11):
    mul = i*table_number
    print(f"{i} x {table_number} = {mul}")
else:
    print("====Done====")