from crypt import methods
from flask import Blueprint
from app.user.controller import UserList, UserCreate, UserId, UserLogin

user_api = Blueprint('user_api', __name__)

user_api.add_url_rule('/cadastro', view_func=UserCreate.as_view('user_create'), methods=['POST'])
user_api.add_url_rule('/users', view_func=UserList.as_view('user_list'), methods=['GET'])
user_api.add_url_rule('/login', view_func=UserLogin.as_view('user_login'), methods=['POST'])
user_api.add_url_rule('/user/<int:id>', view_func=UserId.as_view('user_id'), methods=['GET', 'PUT', 'PATCH', 'DELETE'])
