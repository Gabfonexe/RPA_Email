from flask import jsonify, request
from flask_restful import Resource
from src.service.user import is_user_exist
from extensions import db
from src.model.user import User


class GetUser(Resource):
    def post(self):
        data = request.get_json()
        if data:
            response = is_user_exist(data['email'])
            return jsonify({'success':'Usuário encontrado.'}) if response==True else jsonify({'error': 'Usuário não encontrado.'})
        
            
class GetRepsonse(Resource):
    def get(self):
        return jsonify({'success':'API Iniciada.'})
             

