# Design & create an online store for products (name, price)  
# Track total products being created
# Create a static method to calculate discount on each product based on a % parameter

class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"Price of {self.name} is Rs. {self.price}")

    @classmethod
    def get_count(cls): #ClassMethod
        print(f"The total product created is {cls.count}")

    @staticmethod
    def get_discount(price, discount):
        final_price = price -(discount * price / 100)
        print(f"Your final price after discount is: {final_price}")

p1 = Product("Phone",10_000)
p2 = Product("Pen", 10)
p3 = Product("Laptop", 45_000)

p1.get_info()
p2.get_info()
p3.get_info()

p1.get_discount(10_000,15)
Product.get_count()