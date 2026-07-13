# Creat a class "Employee" and add sallary and increament property to it  

class employee:
    pass

e = employee()

e.sallary = 120000
e.encreament = 10
print(e.sallary, e.encreament)
# but this is not a claas property this is instance property 

# class property

class employee:
    sallary = 12000
    encreament = 9

e = employee

print(e.sallary, e.encreament)