
# from user import User
# from review import Review


class Product:
    """ Class contains the product information """
    def __init__(self, name, description, price, seller, availability=True):
        self.product_name = name
        self.product_description = description
        self.price = price
        self.available = availability
        self.seller = seller
        self.reviews = list()

    def __str__(self):
        return f"{self.product_name}: {self.product_description} "

