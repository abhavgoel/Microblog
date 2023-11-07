from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_object(Config)#configuaration settings from class Config

db=SQLAlchemy(app)# setting up SQLalchemy db interface to interact with db

migrate = Migrate(app,db)

login = LoginManager(app)

login.login_view='login' #regsitering the login view, when users wouldnt be logged in, 
#it would redirect then to this page so that we can use @login_required decorator


from app import routes,models
