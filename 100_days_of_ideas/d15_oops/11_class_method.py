# A method that operates on the class, not the instance. Use @classmethod.

class Product:
    price = 100
    
    @classmethod
    def change_price(cls, new_price):
        cls.price = new_price

Product.change_price(150)
print(Product.price)