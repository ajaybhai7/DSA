class employee():
    name = "None"
    company = "ITC"
    def info(self):
        print(f"Name of employee is {self.name} and the company is  {self.company}")

class Coder():
    language = "Python"
    def printlanguage(self):
        print(f"Out of all the languages here is your language: {self.language}")

# The Class(employee, coder) is parent class of programmmer class
class programmer(employee, Coder):
    company = "ITC infotech"
    def lang(self):
        print(f"Name of employee is {self.name} and her/his language {self.language} is good")

a = employee()
b = programmer()

print(a.company, b.company)

b.info()
b.printlanguage()
b.lang()