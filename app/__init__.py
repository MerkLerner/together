from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# this app is a variable
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# this app is a package (file w init.oy)
from app import routes, models 


''' from the top:
flask runs microblog.pu bc of $FLASK_APP

this accesses "app", which is a python package
(has an init.py, which effectively IS the module

that's this guy!

here's the thing. routes and models need a 
lot of stuff - an actual flask app, a db connection
configuration

so.

in our init.py for the app package

we create a Flask() object, which
we confusingly also label "app"

The diff - the flask object is a real 
python object, the package app is just a module

so there exists an app.app

we also make a db connection

and now, when it's time to kick off routes and models
we have the flask object (app) that they need,
and the database

'''