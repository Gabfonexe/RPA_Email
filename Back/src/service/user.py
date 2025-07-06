from flask import jsonify
from src.service.email import get_email
from extensions import db
from src.model.user import User



def create_user(user:User):

    user_exist = db.session.query(User).filter(user.email==User.email).first()

    if user_exist:
        return jsonify({'error':'Esse E-mail já está cadastrado em nosso banco'})
    
    db.session.add(user)
    db.session.commit()

    return jsonify({'success':'Usuário cadastrado com sucesso!'})


def get_user(email:str):

    user_exist = db.session.query(User).filter(email==User.email).first()

    if user_exist:
       data = {'emails':get_email(user_exist), 'name':user_exist.name}
       return jsonify({'data':data})
    
    return jsonify({'error':'Usuário não encontrado'})


def is_user_exist(email:str):

    is_user = db.session.query(User).filter(email==User.email).first()
    return True if is_user else False

    




