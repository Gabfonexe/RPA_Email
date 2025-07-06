from flask import jsonify
from src.model.user import User
from src.model.email import Email
from utils import message_classification
from extensions import db


def message_validation(msg, name):
    try:
        if not msg:
            return jsonify({'error':'E-mail ausente.'})
        
        response = message_classification(msg, name)
        
        if response:
            return response
        
        return jsonify({'error':'Não foi possível classificar o email e gerar uma resposta. Tente novamente.'})
        
    except Exception as e:
        print(e)
        

def create_email(email:Email):

    db.session.add(email)
    db.session.commit()

    return jsonify({'success':'E-mail cadastrado com sucesso!'})


def get_email(user:User):

    list_emails = db.session.query(Email).filter(user.email==Email.email).all()
    return list_emails

