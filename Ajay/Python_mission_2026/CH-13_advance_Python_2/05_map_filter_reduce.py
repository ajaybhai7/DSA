from functools import reduce
# Map example

l = [1, 2, 3, 4, 5]

square = lambda x: x*x


sqList = map(square, l)
print(list(sqList))

# Filter Example

def even(n):
    if (n % 2 == 0):
        return True
    return False
onlyeven = filter(even, l)
print(list(onlyeven))

# Reduce example

def sum(a, b):
    return a + b

mul = lambda x,y: x*y
print(reduce(sum, l))
print(reduce(mul, l))

# Output
# [1, 4, 9, 16, 25]
# [2, 4]
# 15
# 120
