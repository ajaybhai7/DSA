class employee:
    language = "py" # This is class attribute 
    sallary = 120000


Ajay = employee() #object instetiation 
Ajay.name = "Ajay kumar" # This is a instance attribute
print(Ajay.name, Ajay.language, Ajay.sallary)

rohan = employee()
rohan.name = "Rohan kumar" 
print(rohan.name, rohan.language, rohan.sallary)

# Here name is object attribute and sallary and language are class
# attributes as thety directly belong to the class.

