from flask import Flask
from flask.ext.markdown import Markdown
from flask.ext.login import LoginManager
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py', silent=True)
db = MongoEngine(app)
md = Markdown(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
