class Product:
    def __init__(self, product_name, product_ID, price):
        self.__product_name = product_name
        self.__product_ID = product_ID
        self.__price = price

    def view_product(self):
        print('='*50)
        print(f"Product Name: {self.__product_name}")
        print(f"Product ID: {self.__product_ID}")
        print(f"Product Price: {self.__price}")

    def get_name(self):
        return self.__product_name

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be greater than 0!")



class ShoppingCart:
    def __init__(self):
        self.products_list = []  

    def add_product(self, product):
        if product.get_price() > 0:
            self.products_list.append(product)
            print(f"{product.get_name()} added to cart.")
        else:
            print("Cannot add product with invalid price.")

    def view_cart(self):
        if not self.products_list:
            print("Your cart is empty!")
            return
        print("\n========== Shopping Cart ==========")
        for product in self.products_list:
            product.view_product()
        print("===================================")

    def total_price(self):
        total = 0
        for product in self.products_list:
            total += product.get_price()
        return total



p1 = Product("Laptop", 101, 50000)
p2 = Product("Phone", 102, 30000)
p3 = Product("Headphones", 103, 2000)

cart = ShoppingCart()
cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)

cart.view_cart()
print(f"Total Price: {cart.total_price()}")
