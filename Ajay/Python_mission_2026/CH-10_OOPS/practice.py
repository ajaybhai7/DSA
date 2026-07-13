class employee:
    name = "Ajay"
    age = 20
    sallary = 12000000
    language = "python"
    def getinfo(self):
        print(f"Sallary is : {self.sallary}\nAge is : {self.age}\nName is : {self.name}\nLanguage is : {self.language}")

    @staticmethod
    def greet():
        print("Good Morning")

Ajay = employee()
Ajay.friend = "Vijay"
print(Ajay.friend, Ajay.name, Ajay.sallary, Ajay.age, Ajay.language)
# So pahle ye instance wali argument print hoga fir object ke pass jayega 
# aur tab ja ke niche wale dono function ki requirnment puri hogis
Ajay.getinfo()
Ajay.greet()


