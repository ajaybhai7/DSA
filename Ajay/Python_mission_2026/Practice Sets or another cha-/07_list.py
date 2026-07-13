# list = ['John', 'Mosh', 'Sarah', 'Mary']
# print(list[0:])

# Output: John
''' We Can Esily access any specific name using [0](index)
Such As = The Output Will - John

We Can Also Access Using Nagative index Such As
print(list[-1])
Output: Mary

If the print statement like this 
print(list[0:])
print(list[1:])
print(list[2:])
print(list[:])
print(list[0:-1])
In this list sequence is --> 0,1,2,3,-4,-3,-2,-1 <-- '''

# list = ['John', 'Mosh', 'Sarah', 'Mary']
# print(list)

# Output: ['John', 'Mosh', 'Sarah', 'Mary']

# For Modify Specific item in list 
# such As 

# list = ['John', 'Mosh', 'Sarah', 'Mary']
# list[0] = "Ajay"
# print(list)

# Ooutput: ['Ajay', 'Mosh', 'Sarah', 'Mary']

# Q-1..
# Write a Program to find the largest number in a List.

Numbers = [112, 234, 1231, 413, 13, 1324423]
max = Numbers[0]
for number in Numbers:
    if number > max:
        max = number
print(max)

