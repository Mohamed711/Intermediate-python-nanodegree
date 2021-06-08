import random
import os

from PIL import Image, ImageDraw, ImageFont
from PIL import UnidentifiedImageError


class MemeEngine:

    def __init__(self, output_dir: str):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        self.output_path = os.path.join(output_dir, "img1.jpg")

    def make_meme(self, img_path: str, text, author, width=500) -> str:
        """

        :param img_path:
        :param text:
        :param author:
        :param width:
        :return:
        """
        with Image.open(img_path) as im:

            ratio = width / float(im.size[0])
            height = int(ratio * float(im.size[1]))
            im = im.resize((width, height), Image.NEAREST)

            draw = ImageDraw.Draw(im)
            font = ImageFont.truetype(r'F:\CoursesTaken\Intermediate-'
                                      r'python-nanodegree\Meme Generator Project'
                                      r'\src\MemeGenerator\fonts/LilitaOne-'
                                      r'Regular.ttf', size=20)
            word = text + author
            draw.text((40, 80), word, font=font, fill='red')

            im.save(self.output_path)

        return self.output_path
