# ROSES PDF Generator

PDF Generator micro-service for the [ROSES website](https://github.com/ESHackathon/roses-website).

## Setup

To install the dependencies needed for the application you need to run the following commands
from the project's folder;

``` bash
pip install -r requirements.txt
```

You also need to install [wkhtmltopdf](https://wkhtmltopdf.org/). See their page for installing on the OS
you are using.

## Development

The frontend will be available at [localhost:5000](http://localhost:5000/).

``` bash
FLASK_APP=main.py flask run
```

## Dependency References

Here is a quick list to easily navigate to the documentation of some of the frameworks used in this
app;

 * [Flask](http://flask.pocoo.org/)
 * [Flask-CORS](http://flask-cors.readthedocs.io/en/latest/)
 * [pdfkit](https://pypi.org/project/pdfkit/)
 * [wkhtmltopdf](https://wkhtmltopdf.org/)
