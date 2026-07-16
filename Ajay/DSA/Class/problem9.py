class Bird:
    def __init__(self, Bird_name):
        self.name = Bird_name

    def fly(self):
        print(f"{self.name} Aasman me ud rahi hai")

b1 = Bird("Chidiya")
b1.fly()