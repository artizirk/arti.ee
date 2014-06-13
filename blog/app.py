from flask import Flask
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
db = MongoEngine(app)
