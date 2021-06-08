import random
import os
import requests
import sys
from flask import Flask, render_template, abort, request
from io import BytesIO
from PIL import Image

from QuoteEngine import QuoteModel, Ingestor
from MemeGenerator import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"
    imgs = list(os.listdir(images_path))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)

    images_path = "./_data/photos/dog/"

    path = meme.make_meme(os.path.join(images_path, img),
                          quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    img = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')

    temp_path = os.path.join(os.path.dirname(__file__), "temp.jpg")
    response = requests.get(img)
    im = Image.open(BytesIO(response.content))
    images_path = os.path.abspath("./_data/photos/dog/")
    im.save(temp_path)

    print("-----------------------------------", file=sys.stdout)
    print(os.path.join(images_path, img), file=sys.stderr)
    quote = QuoteModel(body, author)
    path = meme.make_meme(temp_path, quote.body, quote.author)
    # os.remove(temp_path)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
