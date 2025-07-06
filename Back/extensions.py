from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


app =  Flask(__name__)
db =  SQLAlchemy()
ma = Marshmallow()