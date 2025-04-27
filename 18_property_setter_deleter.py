class Product:
    def __init__(self, price):
        self._price = price  
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting the price...")
        del self._price


product = Product(100)

# Accessing the price using the getter
print(product.price) 

# Updating the price using the setter
product.price = 150
print(f"Price has been updated using setter to {product.price}")  # Output: 150

try:
    product.price = -50
except ValueError as e:
    print(e)  

# Deleting the price using the deleter
del product.price  
