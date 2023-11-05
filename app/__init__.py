from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(Config)#configuaration settings from class Config

db=SQLAlchemy(app)# setting up SQLalchemy db interface to interact with db

migrate = Migrate(app,db)

from app import routes,models
