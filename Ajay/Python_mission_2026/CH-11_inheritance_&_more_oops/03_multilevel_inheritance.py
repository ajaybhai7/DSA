class employee:
    def __init__(self):
        super().__init__()
        print("constructor of employee")
    a = 1

class programmer(employee):
    def __init__(self):
        super().__init__()
        print("constructor of programmer")
    b = 2

class manager(programmer):
    def __init__(self):
        super().__init__()
        print("constructor of manager")
    c = 3

o = employee()

print(o.a)# Print the a attribute 
# # print(o.b)# Shows an error as there is no b attribute in employee class

# o = programmer()
# print(o.a, o.b)# print the a, b attribute
# # # print(o.a, o.b, o.c)# Shows an error as there is no c attribute in programmer class 

o = manager()
print(o.a, o.b, o.c)# print the a, b, c attribute
