from extensions import db
from dataclasses import dataclass


@dataclass
class User(db.Model):
    id:int = db.Column(db.Integer, primary_key=True)
    name:str = db.Column(db.String(120), nullable=False)
    email:str = db.Column(db.String(80), nullable=False)
    cellphone:str = db.Column(db.String(16), nullable=False)
    