from flask import request
from flask_restx import Namespace, Resource, fields
from app.messages.model import Message
from app.messages.schemas import MessageSchema

api = Namespace('messages', description='Messages Management')

messages_fields = api.model(
    "Message", { 'title': fields.String, 
                 'text': fields.String,
                 'user_id': fields.Integer }
)

class MessageList(Resource):
    @api.doc(body=messages_fields)
    def post(self):
        data = request.json
        schema = MessageSchema()
        message = schema.load(data)
        message.save()

        return schema.dump(message), 200
    
    def get(self):
        schema = MessageSchema(many=True)
        messages = Message.query.all()

        return schema.dump(messages), 200


api.add_resource(MessageList, '')