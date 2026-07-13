# Add a static method in problem 2, to greet
# the user with hello

class calculator:
    def __init__(self, n):
        self.n = n
    
    @staticmethod
    def greet():
        print("Hello")
    
    def square(self):
        print(f"The square is : {self.n*self.n}")
    
    def cube(self):
        print(f"The cube is : {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The square root is : {self.n**1/2}")

calculator.greet()

s = calculator(n = int(input("Enter Number : ")) )
s.square()

c = calculator(n = int(input("Enter Number : ")) )
c.cube()

sr = calculator(n = int(input("Enter Number : ")) )
sr.squareroot()
