#!/usr/bin/env python

"""Testing Flask with PJAX."""

from argparse import ArgumentParser
from flask import Flask, request, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')


def pjax(template):
    """Test whether the request was with PJAX or not."""
    if "X-PJAX" in request.headers:
        return render_template(template)
    return render_template("base.html", template=template)


@app.route('/')
def home():
    """Render the home page."""
    return pjax('home.html')


@app.route('/planes')
def planes():
    """Render the planes page."""
    return pjax('planes.html')


@app.route('/trains')
def trains():
    """Render the trains page."""
    return pjax('trains.html')


@app.route('/automobiles')
def automobiles():
    """Render the automobiles page."""
    return pjax('automobiles.html')


def find_port():
    """Find the port to run the application on."""
    parser = ArgumentParser()
    parser.add_argument('port', nargs='?', default=5000, type=int,
                        help="An integer for the port you want to use.")
    args = parser.parse_args()
    return args.port


def serve():
    port = find_port()
    app.run(debug=True, host='0.0.0.0', port=port)


if __name__ == '__main__':
    serve()
