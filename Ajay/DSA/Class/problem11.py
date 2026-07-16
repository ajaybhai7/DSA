class Book:
    def __init__(self, tital, auther, pages):
        self.tital = tital
        self.auther = auther
        self.pages = pages

    def read(self):
        print(f"\nAap abhi {self.tital} padh rahe hai, jiske writer {self.auther} hai page no: {self.pages} pe\n")

b1 = Book("Harry Potter", "J.K Rowling", 10)
b1.read()