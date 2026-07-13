# Write a program to print 3rd, 5th and 7th element from a list using enumeration
# Function

l = [1, 4, 5, 2, 5, 3, 2, 4, 1, 1, 2]

for i, item in enumerate(l):
    if i == 0:
        continue
    elif i % 2 == 0:
        print(item)

# output 
# 5
# 5
# 2
# 1
# 2

# According to the q
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i, item in enumerate(l):
    if i == 2 or i == 4 or i == 6:
        print(item)
# Output
# 3
# 5
# 7
