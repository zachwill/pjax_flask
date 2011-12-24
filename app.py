#!/usr/bin/env python

"""Testing Flask with PJAX."""

from flask import Flask, request, render_template

app = Flask(__name__)


def pjax(template):
    """Test whether the request was with PJAX or not."""
    if "X-PJAX" in request.headers:
        return render_template(template)
    return render_template("base.html", template=template)


@app.route('/')
def home():
    """Render the home page."""
    return pjax('home.html')


@app.route('/red')
def red():
    """Render the red color page."""
    return pjax('red.html')


@app.route('/blue')
def blue():
    """Render the blue color page."""
    return pjax('blue.html')


@app.route('/green')
def green():
    """Render the green color page."""
    return pjax('green.html')
