# Write a program to open three file 1.txt, 2.txt and 3.txt if any these file are not present, 
# a message without exiting the program must be printed promoting the same
try:
    with open("1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e) 

try:
    with open("2.txt") as f:
        a = f.read()
        print(a)

except Exception as e:
    print(e)

try:
    with open("3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)


print("End of the program")
# Output
# [Errno 2] No such file or directory: '1.txt'
# [Errno 2] No such file or directory: '2.txt'
# [Errno 2] No such file or directory: '3.txt'

# after making 2.txt file output is: 

# Output
# [Errno 2] No such file or directory: '1.txt'
# Hi i am file 2

# [Errno 2] No such file or directory: '3.txt'
