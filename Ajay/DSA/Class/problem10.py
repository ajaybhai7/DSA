class Dog:
    def __init__(self, dog_name):
        self.name = dog_name

    def bark(self):
        print(f"\n{self.name} jor se bhaunk raha hai: Bhow Bhow!\n")

d1 = Dog("Honey")
d1.bark()