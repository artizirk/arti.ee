from flask.ext.script import Manager, Server
from flask_debugtoolbar import DebugToolbarExtension

from blog import app

app.config["DEBUG"] = True
toolbar = DebugToolbarExtension(app)
manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0"))

if __name__ == "__main__":
    manager.run()
