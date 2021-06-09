import os
from abc import ABC, abstractmethod


class MemeEngineInterface(ABC):
    """ Interface class for the Meme Engines """

    def __init__(self, output_dir: str):
        """
        Create a meme on a given image
        :param output_dir: The output directory of the
                           created image
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        self.output_dir = output_dir

    @abstractmethod
    def make_meme(self, img_path: str, text: str,
                  author: str, width=500) -> str:
        """
        Create a meme on a given image
        :param img_path:  The path of the image
        :param text: The text of the quote to be added
        :param author: The author of the quote
        :param width: Resize the image to this width
        :return: The path of the output image
        """
        pass
