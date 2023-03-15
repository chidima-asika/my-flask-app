from flask import Flask

def create_app():
    app = Flask(__name__) #how Flask is initialized
    app.config["SECRET_KEY"] = "ihaveasecret13793"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') #prefix tells you how to access them
    app.register_blueprint(auth, url_prefix='/')

    return app


