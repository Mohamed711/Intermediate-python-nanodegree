import subprocess
import os
from typing import List

from .IngestorInterface import IngestorInterface, IngestorError
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """ Extract the quotes information from PDF files """

    supported_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Extract Quote information from PDF files
        :param path: Path of the file
        :return: List of the QuoteModels in this file
        """
        if not cls.can_ingest(path):
            raise IngestorError(f'Parse is called with wrong type')

        temp_path = os.path.join(os.path.dirname(__file__), "PDFtoTxt.txt")

        # Ensure the temp file is deleted
        if os.path.exists(temp_path):
            os.remove(temp_path)

        subprocess.call(['pdftotext', path, temp_path])
        quotes = list()

        with open(temp_path, "r") as file_ref:
            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split('-')
                    quote = QuoteModel(parse[0], parse[1])
                    quotes.append(quote)

        os.remove(temp_path)
        return quotes
