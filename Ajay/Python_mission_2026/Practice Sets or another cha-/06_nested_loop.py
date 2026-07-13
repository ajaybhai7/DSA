# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")


# xxxxx
# xx
# xxxxx
# xx
# xx

number = [5, 2, 5, 2, 2]
for n in number:
    print(n*"x")

# Using Inner Loop

Number = [5, 2, 5, 2, 2]
for x_count in Number:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)