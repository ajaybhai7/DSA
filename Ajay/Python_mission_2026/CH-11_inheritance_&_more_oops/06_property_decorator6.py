class employee:
    a = 1
    @classmethod
    def show(cls):# print class attribute of a means class define a = 1
        print(f"The class attribute of a is {cls.a}")
# Output: The class attribute of a is 1
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name (self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


    def show1(self):# it will show instance attribute meand instancee define e.a = 42
        print(f"The class attribute of a is {self.a}")
# Output: The class attribute of a is 42

e = employee()
e.a = 42
e.show()
e.show1()
e.name = "Ajay Kumar"

print(e.lname)

