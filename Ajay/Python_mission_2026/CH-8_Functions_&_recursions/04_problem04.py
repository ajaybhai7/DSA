# write a program to print first n line of the following pattern
# ***
# **
# * for n = 3

def pattern(n):
    if (n==0):
        return
    print("*" * n)
    pattern(n-1)
pattern(5)