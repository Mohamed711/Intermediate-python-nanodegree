

class QuoteModel:

    def __init__(self, quote: str, author: str):
        """
        Initialize a new quote
        :param quote: The body of the quote
        :param author: The author of the quote
        """
        self.quote = quote
        self.author = author

    def __repr__(self):
        return f'"{self.quote}" - {self.author}'
