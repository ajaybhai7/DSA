import array as arr # importing array module and giving it an alias name arr

val  = arr.array("I", [1, 2, 3, 4, 5, 6]) # creating an array of unsigned integers
print(f"\nArray: \n{val}\n") # printing the array


for i in range (0, 6):
    print(f"{val[i]}", end=" ")

print("\n")

for x in val: # this is called enhanced for loop,
    #  it is used to iterate over the elements of an array
    print(f"{x}", end=", ")
