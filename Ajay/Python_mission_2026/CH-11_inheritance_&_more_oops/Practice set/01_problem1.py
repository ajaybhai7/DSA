# creat a class (2-D vector) and use it to create another class representing a
# 3-D vector

class twoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The 2-D vector is = {self.i}i + {self.j}j")

class ThreeDVector():
    def __init__(self, i, j, k):
        # super().__init__(i, j) # it helps to reduce line that already
        # wrote in base(parent class) after this we dont need to write those 
        # two argument that is already written in base class 
        # class ThreeDVector(twoDVector)
        self.i = i
        self.j = j
        self.k = k

    def show(self):
        print(f"The 3-D vector is = {self.i}i + {self.j}j + {self.k}k")

a = twoDVector(1, 2)
b = ThreeDVector(1, 2, 3)

a.show()
b.show()