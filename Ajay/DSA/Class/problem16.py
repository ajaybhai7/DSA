class ShoppingCart:
    def __init__(self, costomer_name):
        self.name = costomer_name
        self.cart = []

    def add_item(self, item_name):
        self.cart.append(item_name)

    def show_cart(self):
        if len(self.cart) != 0:
            print(f'''
{self.name} Your Cart is ->
                {self.cart}''')

c1 = ShoppingCart("Ajay")            
c1.add_item(input("Add Item: "))
c1.show_cart()
