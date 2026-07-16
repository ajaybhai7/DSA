class Calculator:
    def add(self, num1, num2):
        total = num1 + num2
        print(f"{num1} + {num2} = {total}")
    
    def subtract(self, num1, num2):
        total = num1 - num2
        print(f"{num1} - {num2} = {total}")
    
my_calc = Calculator()
my_calc.add(num1=int(input("Enter Your First Number: ")), num2=int(input("Enter Your Second Number: ")))
my_calc.subtract(num1=int(input("Enter Your First Number: ")), num2=int(input("Enter Your Second Number: ")))


    