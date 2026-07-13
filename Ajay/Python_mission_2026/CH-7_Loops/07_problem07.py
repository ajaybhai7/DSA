# Write a program to print the following star patter
#   *
#  ***
# ***** for n = 3

n = int(input("Enter a Number >")) 
i = 1
while i <= n:
    print(" "*(n-i), end="")
    print("*" * (i*2-1) )
    i += 1
