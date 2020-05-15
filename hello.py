import os
from flask import Flask
from flask import render_template, send_from_directory
from urlparse import urlparse, urlunparse

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Agarwal' } # fake user
    return render_template("index.html",
        title = 'Home',
        user = user)

@app.route('/resume')
def resume():
    return send_from_directory('static', 'resume.pdf')

if __name__ == '__main__':
    app.run(debug=True)

