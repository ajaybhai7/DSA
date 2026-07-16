class Employee:
    def __init__(self, Name, Sallary):
        self.name = Name
        self.sallary = Sallary

    def anual_sallary(self):
        print(f'''
                Name                -> {self.name}
                Monthly Sallary     -> {self.sallary}
                Anual Sallary       -> {self.sallary * 12}''')

name = (input("Enter Employee Name: "))
salary = (int(input("Enter Employee Monthly Sallary: ")))

majdur = Employee(name, salary)

majdur.anual_sallary()
