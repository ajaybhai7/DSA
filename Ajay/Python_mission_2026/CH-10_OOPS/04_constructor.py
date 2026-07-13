class employees:
    name = "Ajay"
    age  = 20
    language = "python"

    def __init__(self, name, age, language): # Dunder method which is automatically self called
        self.name = name
        self.age = age
        self.language = language
        print("I am creating an objecct")

        
    def getinfo(self):
        print(f"This name is: {self.name}\nThis age is : {self.age}\nThis language is : {self.language}")
    @staticmethod # It's dont Need Any self Parameter in the function like
    #def greet(self):
    #   print("Good Morning")
    def greet():
        print("Good Morning")

Ajay = employees("Ajay", 21, "Javascrippt") 
rohit = employees("Roht", 23, "Assembly")
print(Ajay.name, Ajay.age, Ajay.language)
print(rohit.name, rohit.age, rohit.language)
              