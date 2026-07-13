from numpy import *

# val = array([1, 3, 5, 6, 7, 8, 6, 3, "a"])
# val = array([1, 3, 5, 6, 7, 8, 6, 3, "a"], str)

# for x in val:
#     print(x, end=" ")

val1 = linspace(1, 20, 10).round() # 1 is first parameter where count start
# 20 is last parameter where line end 
# 10 is parameter to devide into 10 parts of 1 to 20 numbers
for y in val1:
    print(y, end=" ")

# Output
# 1.0 3.0 5.0 7.0 9.0 12.0 14.0 16.0 18.0 20.0

a = arange(1, 20, 4)
print(a)
# Output
# 1 -4- 5 -4- 9 -4- 13 -4- 17
# 1 is the first eliment where number start
# 20 is the eliment where numbers end
# 4 is the eliment how gap between the numbers 1 to 20 

b = zeros(10)
c = ones(10)
d = full(10, 5)

print(f"{b}\n{c}\n{d}")

# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] = b
# [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.] = c
# [5 5 5 5 5 5 5 5 5 5] = d

