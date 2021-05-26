# from product import Product
# from user import User


class Review:
    """ Class contains the review information """
    def __init__(self, description, user, product):
        self.description = description
        self.user = user
        self.product = product
