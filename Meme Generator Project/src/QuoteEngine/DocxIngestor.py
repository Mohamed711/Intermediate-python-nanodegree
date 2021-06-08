import docx
from typing import List


from .IngestorInterface import IngestorInterface, IngestorError
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """ Extract the quotes information from Docx files """

    supported_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Extract Quote information from Docx files
        :param path: Path of the file
        :return: List of the QuoteModels in this file
        """
        if not cls.can_ingest(path):
            raise IngestorError(f'Parse is called with wrong type')

        quotes = list()
        doc = docx.Document(path)

        for paragraph in doc.paragraphs:
            if paragraph.text != "":
                parse = paragraph.text.split('-')
                quote = QuoteModel(parse[0], parse[1])
                quotes.append(quote)

        return quotes
