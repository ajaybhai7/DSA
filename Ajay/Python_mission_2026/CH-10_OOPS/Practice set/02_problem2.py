# Write a class "Calculator" capable of finding square, cube and square root
# of a number

class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is : {self.n*self.n}")

    def cube(self):
        print(f"The cube is : {self.n*self.n*self.n}")

    def square_root(self):
        print(f"The square root is : {self.n**1/2} ")

s = calculator(n=int(input("Enter Number for square: ")))
s.square()

c = calculator(n=int(input("Enter number For Cube: ")))
c.cube()

sr = calculator(n = int(input("Enter Number for square root: ")))
sr.square_root()

