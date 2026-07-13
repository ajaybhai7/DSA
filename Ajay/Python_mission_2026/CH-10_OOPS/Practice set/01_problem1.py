# Creat a class "programmer" for storing information of few programmerce
# Working at microsoft

class programmers:
    company = "Microsoft"

    def __init__(self, name, sallary, pin):
        self.name = name
        self.sallary = sallary
        self.pin = pin

p = programmers("Ajay", 120000, 110017)
print(p.name, p.sallary, p.pin, p.company)

r = programmers("Rohan", 15000, 245533)
print(r.company, r.name, r.sallary, r.pin)

