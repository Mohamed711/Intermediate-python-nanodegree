
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """
    Quote Ingestor abstract class to be realized by different
    ingestor engines
    """

    supported_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the file extension is supported or not
        :param path: path of the file
        :return: True: File extension is supported, False otherwise
        """
        extension = path.split(".")[-1]
        return extension in cls.supported_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the file according to its extension
        :param path: Path of the file
        :return: List of the QuoteModels in this file
        """
        pass
