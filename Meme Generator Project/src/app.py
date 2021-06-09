import random
import os
import requests

from requests import RequestException
from flask import Flask, render_template, request
from pathlib import Path

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

    quotes = list()
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    # Read all files from the given path
    imgs = list()
    for root, dirs, files in os.walk(images_path):
        for file in files:
            imgs.append(os.path.join(root, file))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # Read the form parameters
    img = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')

    try:
        response = requests.get(img, allow_redirects=True)
    except RequestException:
        print("Can't accees the given image URL")

    # save the image in a temporary file
    temp_file = Path(f'./tmp/{random.randint(0, 100000000)}.png')
    temp_file.parent.mkdir(exist_ok=True)
    open(temp_file, 'wb').write(response.content)

    # create the meme using the temporary downloaded image
    quote = QuoteModel(body, author)
    path = meme.make_meme(temp_file, quote.body, quote.author)

    temp_file.unlink(missing_ok=True)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
