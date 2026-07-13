import array


val = array.array("I", [1, 2, 3, 4, 5, 6])
print(f"\nArray: \n{val}\n")
for i in range(0, 6):
    print(val[i], end=" ")

print("\n")

for x in val:
    print(f"{x}", end=", ")