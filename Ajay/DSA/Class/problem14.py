class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f'''
The Area of Rectangle ->
            length x Width = {self.length * self.width}''')

a = Rectangle(None , None)
a.length = int(input("Enter Length of the trangle -> "))
a.width = int(input("Enter width of the trangle -> "))

a.area()