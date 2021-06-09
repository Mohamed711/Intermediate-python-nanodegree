from .MemeEngineInterface import MemeEngineInterface
from .PILMemeEngine import PILMemeEngine


class ImageNotSupported(NotImplementedError):
    pass


class MemeEngine(MemeEngineInterface):
    """
    This class creates a meme on a given image abstracting
    the caller from the used library to create this meme
    """

    def make_meme(self, img_path: str, text: str,
                  author: str, width=500) -> str:
        """
        Select the meme engine based on the
        image extension
        :param img_path:  The path of the image
        :param text: The text of the quote to be added
        :param author: The author of the quote
        :param width: Resize the image to this width
        :return: The path of the output image
        """

        # This shall select the engine either
        # based on the extension or anything else
        extension = str(img_path).split(".")[-1]
        if extension.lower() == "jpg" or extension.lower() == "png":
            return PILMemeEngine(self.output_dir).\
                make_meme(img_path, text, author, width)
        else:
            raise ImageNotSupported(f'The given image with extension '
                                    f'{extensions} is not supported yet')
