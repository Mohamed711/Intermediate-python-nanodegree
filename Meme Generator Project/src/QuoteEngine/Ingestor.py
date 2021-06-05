from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TxtIngestor import TxtIngestor


class Ingestor(IngestorInterface):
    """ Select the appropriate ingestor """

    supported_ingestors = [CSVIngestor, PDFIngestor, TxtIngestor, DocxIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the content of the file based on its extension
        :param path: Path of the file
        :return: List of quotes from this file
        """
        for ingestor in cls.supported_ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
