class Person:
    def __init__(self, person_name):
        self.name = person_name

p1 = Person("Ajay")
p2 = Person("Vijay")

print(f"Pehla Aadmi: {p1.name}\nDusra Aadmi: {p2.name}")