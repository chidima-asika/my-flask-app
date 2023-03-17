# not related to authentification and the user can see, will go here

from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/') #root for home page
@login_required
def home():
    return render_template("home.html", user=current_user)
    

