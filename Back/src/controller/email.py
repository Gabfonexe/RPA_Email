from flask_restful import Resource
from flask import json, jsonify, request
from utils import extract_pdf, extract_txt, preprocess_text
from src.service.email import message_validation
from src.service.user import create_user, get_user
from src.service.email import create_email
from src.model.email import Email
from src.model.user import User

class CreateEmail(Resource):
    def post(self):
        data = json.loads(request.form.get('data'))
        file = request.files.get('file')
        message = {}
        if data:
            user = create_user(User(name=data['name'], email=data['email'], cellphone=data['cellphone']))
            
            if file:
                if file.filename.endswith('.pdf') or file.mimetype == 'application/pdf':
                    file.stream.seek(0)
                    content = extract_pdf(file)
                elif file.filename.endswith('.txt') or file.mimetype == 'text/plain':
                    content = extract_txt(file)
                
                if content:
                    processed_content = preprocess_text(content)
                    message = message_validation(processed_content, data['name'])   
                 
            if not file:
                processed_message = preprocess_text(data['message'])
                message = message_validation(processed_message, data['name'])

            email = create_email(Email(message=message['message'], classification=message['classification'], email=data['email']))

            if email and user:
                return jsonify({'success': 'Resposta ao email enviado com sucesso'})


class GetEmails(Resource):

    def post(self):

        data = request.get_json()
        if data:
            response = get_user(data['email'])
            return  response
        
        return jsonify({'error':'Email ausente.'})










