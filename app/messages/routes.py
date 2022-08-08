from flask import Blueprint
from app.messages.controller import MessageCreateAndList

message_api = Blueprint('message_api', __name__)

message_api.add_url_rule('/message', view_func=MessageCreateAndList.as_view('msg_c_l'), methods=['POST', 'GET'])