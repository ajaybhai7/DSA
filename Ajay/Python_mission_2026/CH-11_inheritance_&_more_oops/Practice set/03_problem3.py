# creat a class 'Pets' from a class 'Animals' and further creat a class 'Dog'
# from 'Pets. Add a method 'bark' to class dog 

class Animals:
    pass

class Pets(Animals): # This is called inharance
    pass

class Dog(Pets): # This is called inharance
    @staticmethod # it use to print withouth any argument or self method
    def bark():
        print("Bow Bow!")
    pass

d = Dog
d.bark()

