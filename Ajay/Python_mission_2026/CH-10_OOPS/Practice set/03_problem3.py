# Creat a class with a class attribute a; creat an object from it and set 'a'
# direcctly using object.a = 0 does this change the class attribute.

class demo:
    a = 4

o = demo()
print(o.a)
#prints class attribute because instance attribute
# is not present
o.a = 0 # instance attribute set
print(o.a) # prints the instance attribute 
# because the instance attribute is present

print(demo.a) # Prints the class attribute
# The Output will be: 
"""
4 first output
0 second output
"""

