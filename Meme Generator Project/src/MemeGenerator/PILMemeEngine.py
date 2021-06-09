import random
import os

from PIL import Image, ImageDraw, ImageFont
from PIL import UnidentifiedImageError

from .MemeEngineInterface import MemeEngineInterface


class PILMemeEngine(MemeEngineInterface):
    """ Add meme to the given image using the PILLOW library """

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
        try:
            im = Image.open(img_path)

            # Resize the image
            ratio = width / float(im.size[0])
            height = int(ratio * float(im.size[1]))
            im = im.resize((width, height), Image.NEAREST)

            # Add the quote to the given image
            draw = ImageDraw.Draw(im)
            font = ImageFont.truetype(r'./_data/fonts/LilitaOne-Regular.ttf',
                                      size=20)
            word = f'{text} {author}'
            quote_location = (random.randint(0, width/4),
                              random.randint(0, int(0.75 * height)))
            draw.text(quote_location, word, font=font, fill='red')

            output_file = os.path.join(self.output_dir,
                                       os.path.basename(img_path))
            im.save(output_file)

        except UnidentifiedImageError:
            print("Can't load a valid image from the given url")

        except FileNotFoundError:
            print("The input image file path can not be found")

        return output_file
