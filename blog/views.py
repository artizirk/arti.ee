import os
from . import app
from flask import render_template, send_from_directory


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'img'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route("/")
def index():
    return render_template("index.html")
