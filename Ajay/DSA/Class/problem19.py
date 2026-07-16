class PhoneBook:
    def __init__(self, owner_name):
        self.owner = owner_name
        self.contact = {}

    def add_contact(self, name, phone_number):
        self.contact[name] = phone_number

    def show_contact(self):
        print(f'''
owner = {self.owner}\nContact -> {self.contact}''')

p1 = PhoneBook("Ajay")
p1.add_contact(name=input("Enter Name: "), phone_number=int(input("Enter Number: ")))
p1.show_contact()