from product import Product
from review import Review


class User:
    """ Class contains the user information """
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.username = name
        self.reviews = list()

    def sell_product(self, name, description, price):
        return Product(name, description, price, self, True)

    def buy_product(self, prod: Product):
        if prod.available is True:
            prod.seller = self
            prod.available = False
        else:
            print(f"{prod} is not available")

    def write_review(self, review_description, prod: Product):
        review = Review(review_description, self, prod)
        self.reviews.append(review)
        prod.reviews.append(review)
        return review

