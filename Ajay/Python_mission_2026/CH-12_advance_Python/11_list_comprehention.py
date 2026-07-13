myList = [1, 3, 5, 8, 3, 2]

squarelist = []

for item in myList:
    squarelist.append(item)

print(squarelist)

# Output

# [1, 3, 5, 8, 3, 2]

myList = [1, 3, 5, 8, 3, 2]

squarelist = []

for item in myList:
    squarelist.append(item*item)

print(squarelist)

# Output

# [1, 9, 25, 64, 9, 4]

# in comprehention

myList = [1, 3, 5, 8, 3, 2]

squarelist = [i*i for i in myList]

print(squarelist)

# Similar work with a less line of code
