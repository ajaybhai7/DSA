# Creat a class "Employee" and add sallary and increament property to it  
# Write a method 'salaryAfterencreament' method with a @property decorator
# with a setter which changes the value of increament based on the sallary

class employee:
    sallary = 124400
    increament = 9

    @property
    def salaryAfterencreament(self):
        return (self.sallary + self.sallary * (self.increament/100))
    @salaryAfterencreament.setter
    def salaryAfterencreament(self, sallary):
        self.increament = (sallary-self.sallary) 
        
e = employee()
print(f"The base sallary is = {e.sallary}")
print(f"After increamt the sallary is : {e.salaryAfterencreament}")
e.salaryAfterencreament = e.salaryAfterencreament
print(f"The amount is added on sallary as increamet is = {e.increament}")