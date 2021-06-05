
from .IngestorInterface import IngestorInterface, IngestorError
from typing import List
from .QuoteModel import QuoteModel


class TxtIngestor(IngestorInterface):
    """ Extract the quotes information from text files """

    supported_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Extract Quote information from txt files
        :param path: Path of the file
        :return: List of the QuoteModels in this file
        """
        if not cls.can_ingest(path):
            raise IngestorError(f'Parse is called with wrong type')

        quotes = list()

        with open(path, 'r') as input_file:
            for line in input_file:
                if line:
                    parsed_quote = line.split('-')
                    quote = QuoteModel(parsed_quote[0], parsed_quote[1])
                    quotes.append(quote)

        return quotes
