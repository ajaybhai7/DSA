class Laptop:
    def __init__(self, lap_brand, lap_ram):
        self.brand = lap_brand
        self.ram = lap_ram

l1 = Laptop("Lenovo", "16GB")
l2 = Laptop("Acer", "32GB")

print(f"\n====Laptop 1====\nBrand Name : {l1.brand}\nTotal RAM: {l1.ram}\n")
print(f"\n====Laptop 2====\nBrand Name : {l2.brand}\nTotal RAM: {l2.ram}\n")
