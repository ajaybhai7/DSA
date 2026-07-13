from array import *

val  = array("I", [1, 2, 3, 4, 5, 6]) # creating an array of unsigned integers
print(f"\nArray: \n{val}\n") # printing the array


for i in range (0, len(val)):
    print(f"{val[i]}", end=" ")

print("\n")

for x in val: # this is called enhanced for loop,
    #  it is used to iterate over the elements of an array
    print(f"{x}", end=", ")

# for float

val2  = array("f", [1, 2, 3, 4, 5, 6, 7, 8, 9, 9.5]) # creating an array of float
print("\n")
for num in val2:
    print(num, end=" ")

# for  unicode
val3  = array("w", ['a', 'b', 'c', 'd', 'e', 'f']) # creating an array of unicode
print("\n")
for char in val3:
    print(char, end=" ")

# for reverse

val.reverse()

for a in val:
    print(a)

