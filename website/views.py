# not related to authentification and the user can see, will go here

from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/') #root for home page
def home():
    return "<h1>Test</h1>"
    

