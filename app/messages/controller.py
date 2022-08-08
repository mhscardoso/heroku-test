from flask import jsonify, request
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from app.messages.model import Message
from app.messages.schemas import MessageSchema


class MessageCreateAndList(MethodView):
    decorators = [jwt_required()]
    def post(self):
        data = request.json
        schema = MessageSchema()
        message = schema.load(data)
        message.save()

        return jsonify(schema.dump(message)), 200
    

    def get(self):
        schema = MessageSchema(many=True)
        messages = Message.query.all()

        return schema.dump(messages), 200


