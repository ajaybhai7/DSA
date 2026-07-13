# i = 1
# while i <= 50:
#     print(i)
#     i += 1


# num = int(input("Enter number to print > "))
# i = 0
# while i <= num:
#     print(i)
#     i +=1 


# num = int(input("Enter number to Print Only ODD Numbers > "))

# i = 1

# while i <= num:
#     if i % 2 != 0:
#         print(i)
#     i +=1

# num = int(input("Enter Number to print only even Numbers > "))

# i = 1

# while i <= num:
#     if i % 2 == 0:
#         print(i)
#     i += 1


# to simplyfy this 

# num = int(input("Enter number > "))
# choose = input("Choose (odd/even): ")
# i = 1

# while i <= num:
#     if choose.lower() == "even" and i % 2 == 0:
#         print(i)
#     elif choose.lower() == "odd" and i % 2 != 0:
#         print(i)
#     i += 1


num = int(input("Enter number > "))
i = 1
while i <= num:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i +=1
