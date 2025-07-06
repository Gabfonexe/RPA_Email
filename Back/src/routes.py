from src.controller.email import CreateEmail, GetEmails
from src.controller.user import GetUser

def register_routes(api):
    api.add_resource(CreateEmail, '/create_email')
    api.add_resource(GetEmails, '/get_user')
    api.add_resource(GetUser, '/is_user')


   