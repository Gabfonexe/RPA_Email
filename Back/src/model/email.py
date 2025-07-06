from dataclasses import dataclass
from flask import json
from extensions import db, ma


@dataclass
class Email(db.Model):
    id:int = db.Column(db.Integer, primary_key=True)
    message:str = db.Column(db.Text)
    classification:str = db.Column(db.String(20))
    email:str = db.Column(db.String(80))

    

