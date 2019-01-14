from flask import Flask

print( __name__)

# this app is a variable
app = Flask(__name__)

# this app is a package (file w init.oy)
from app import routes 


'''wild. okay. so, app is this whole directory.
in the context of the import statement.

from app <-- that's this folder. 

so we're saying, looking in all the files from this folder, and find the routes module(py file really)

this is that circular import thing.

the whole thing is kicked of by microblog.py

I think when it imports app as a package, python fires
__init__.py

this, in turn, creates a flask app object and imports routes

the confusing thing: routes imports the app object from 
the app directory (which was an awful teaching move)

i think it does this because of module type behavior 
- each has their own scope'''