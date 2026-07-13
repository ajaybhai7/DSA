class twoDVector:
    def __init__(self, i, j):
        print("===== 2-D Vector =====")
        # i = 1
        i = int(input("Enter Number > "))
        # j = 2
        j = int(input("Enter Number > "))
        self.i = i
        self.j = j

    def show(self):
        print(f"The 2-D Vector is : {self.i}i + {self.j}j")

class threeDVector:
    def __init__(self, i, j, k):
        print("===== 3-D Vector =====")
        # i = 5 # We can also take input from the user for costom vector number
        i = int(input("Enter Number > "))
        # j = 10
        j = int(input("Enter Number > "))
        # k = 0
        k = int(input("Enter Number > "))
        self.i = i
        self.j = j
        self.k = k

    def show(self):
        print(f"The 3-D Vector is = {self.i}i + {self.j}j + {self.k}k")


a = twoDVector(3, 5)
b = threeDVector(1, 2, 3)

a.show()
b.show()

