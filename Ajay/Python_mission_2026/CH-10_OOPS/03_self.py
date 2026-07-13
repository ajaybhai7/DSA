class employees:
    name = "Ajay"
    age  = 20
    Language = "python"

    def getinfo(self):
        print(f"This name is: {self.name}\nThis age is : {self.age}\nThis language is : {self.Language}")
    @staticmethod # It's dont Need Any self Parameter in the function like
    #def greet(self):
    #   print("Good Morning")
    def greet():
        print("Good Morning")

Ajay = employees()
Ajay.getinfo()
Ajay.greet()


              