class Customer:

    def __init__(self, first_name, surname, tier=('free', 0)):
        self.first = first_name
        self.second = surname
        self._tier = tier[0]
        self._cost = tier[1]

    @property
    def name(self):
        """ Get the name """
        return f"{self.first} {self.second}"

    def can_access(self, content):
        return content['tier'] == 'free' or content['tier'] == self._tier

    @classmethod
    def premium(cls, first, second):
        return cls(first, second)

    def bill_for(self, months):
        return self._cost * months


if __name__ == '__main__':
    # This won't run until you implement the `Customer` class!

    marco = Customer('Marco', 'Polo')  # Defaults to the free tier
    print(marco.name)  # Marco Polo
    print(marco.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
    print(marco.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # False

    victoria = Customer.premium("Alexandrina",
                                "Victoria")  # Build a customer around the ('premium', 10$/mo) streaming plan.
    print(victoria.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
    print(victoria.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # True
    print(victoria.bill_for(5))  # => 50 (5 months at 10$/mo)
    print(victoria.name)  # Alexandrina Victoria

