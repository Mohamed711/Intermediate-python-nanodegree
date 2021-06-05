import pandas as pd
from typing import List

from .IngestorInterface import IngestorInterface, IngestorError
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """ Extract the quotes information from CSV files """

    supported_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Extract Quote information from CSV files
        :param path: Path of the file
        :return: List of the QuoteModels in this file
        """
        if not cls.can_ingest(path):
            raise IngestorError(f'Parse is called with wrong type')

        quotes = list()
        quotes_df = pd.read_csv(path, header=0)

        for _, parsed_quote in quotes_df.iterrows():
            quote = QuoteModel(parsed_quote['body'], parsed_quote['author'])
            quotes.append(quote)

        return quotes


