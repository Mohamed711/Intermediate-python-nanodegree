# Intermediate Python Udacity Nanodegree: Meme Generator Project

This project is a simple meme generator project. It is used to generator different quotes 
on different images.

The project has a command line interface (CLI) and a web interface. The command line interface
can be used to specify the image and the required quote.

Also, you can use the web interface to enter the image URL and the required quote 
to be added on this image.

The project will use default quotes and images in case of input missing paramters.

## Project Setup
For python libraries dependencies installation please follow the following steps

* Run this command "{PYTHON_3} -m venv venv" at the project path to create a virtual 
environment in "venv" folder. {PYTHON_3} is the python 3 version exe file 
name (ex: python).

* Activate the virtual environment using "<venv>\Scripts\activate.bat" for windows users and using "source <venv>/bin/activate"
for linux users

* From the virtual environment prompt, install all the dependencies from the requirements.txt
file using the following command "{PYTHON_3} -m pip install -r requirements.txt"

* To enable the web interface, change directory inside the "Src" folder and run the 
following command "flask run --host 0.0.0.0 --port 3000".

* You can run the meme.py file giving the required parameters from the command line
"{PYTHON_3} meme.py --path {image_path} --body {quote body} --author {author name}".

## Project Structure

* app           : Run the meme generator from the web interface
* meme   	    : Run the meme generator from the CLI
* QuoteEngine	: Contains structure and methods related to the quote handling 
    * CSVIngestor       : Read quotes from CSV file format
    * DocxIngestor      : Read quotes from Docx file format
    * PDFIngestor       : Read quotes from PDF file format
    * TextIngestor      : Read quotes from text file format
    * IngestorInterface : Abstract class for different quotes ingestors
    * Ingestor          : Invoke the appropriate ingestor according to the file extension
    * QuoteModel        : Quote information object
* MemeGenerator : Contains structure and methods related to the meme generation handling
    * MemeEngine        : Invoke the appropriate meme engine
    * MemeEngineInterface: Abstract class to define the different meme engines
    * PILMemeEngine     : MemeEngine using Pillow library for "jpg" and "png" images

* _data 		: contains different sample data including images 
and quotes in different file formats
* templates     : contains the html templates for the web interface

