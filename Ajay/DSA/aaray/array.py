import array

array1 = array.array("i", [1, 2, 3, 4, 5, 6])

print(f"This is Array of : {array1}")

for i in range(0, 6):
    print(array1[i], end=" ")

print("\n")

for array in array1: # this is called enhanced for loop, 
    # it is used to iterate over the elements of an array
    print(f"{array}", end=" ")


val = array.array("I", [1, 2, 3, 4, 5, 6])
print(val)

for i in range(0, 6):
    print(val[i], end=" ")

print("\n")

for x in val:
    print(f"{x}", end=" ")
