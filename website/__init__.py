from flask import Flask
from . import dynamo_db

def create_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'random string called cheese-pizza'

    # importing blueprints
    from .views import views
    from .auth import auth

    # registering
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    create_database()

    return app

def create_database():
    dynamo_db.create_users_table()
