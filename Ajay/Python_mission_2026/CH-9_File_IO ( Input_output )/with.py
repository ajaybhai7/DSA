file = open("file.txt")
print(file.read())
file.close()

''' the same can be written using with statement 
like this'''

with open("file.txt")as file:
    print(file.read())

# You dont have to explicitly close the file 