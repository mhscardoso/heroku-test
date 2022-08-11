from flask import request
from flask_jwt_extended import create_access_token, jwt_required
from flask_restx import Namespace, Resource, fields
from app.utils.filter import filters
from app.user.model import User
from app.user.schemas import UserSchema, UserLoginSchema
import bcrypt

api = Namespace('users', description='User Management')

user_fields = api.model(
    "User", { 'username': fields.String, 
              'password': fields.String }
)

class UserList(Resource):
    def get(self):
        schema = filters.getSchema(qs=request.args, schema_cls=UserSchema, many=True)
        users = User.query.all()
        return schema.dump(users), 200

    @api.doc(body=user_fields)
    def post(self):
        data = request.json
        schema = UserSchema()
        user = schema.load(data)
        user.save()
        return schema.dump(user), 201


class UserId(Resource):
    decorators = [jwt_required()]
    @api.doc(security='apikey')
    def get(self, id):
        schema = filters.getSchema(qs=request.args, schema_cls=UserSchema)
        user = User.query.get_or_404(id)
        return schema.dump(user), 200

    @api.doc(body=user_fields, security='apikey')
    def put(self, id):
        try:
            user = User.query.get_or_404(id)
        except:
            return {"error": "User not found"}, 404
        
        data = request.json
        schema = UserSchema(exclude=["password"])
        user = schema.load(data, instance=user)

        user.update()
        return schema.dump(user), 200
    
    @api.doc(body=user_fields, security='apikey')
    def patch(self, id):
        try:
            user = User.query.get_or_404(id)
        except:
            return {"error": "User not found"}, 404
        
        data = request.json
        schema = UserSchema(exclude=['password'])
        user = schema.load(data, instance=user, partial=True)

        user.update()
        return schema.dump(user), 200

    @api.doc(security='apikey')
    def delete(self, id):
        try:
            user = User.query.get_or_404(id)
        except:
            return {'error': 'User not found'}, 404
        
        User.delete(user)
        return {}, 204


class UserLogin(Resource):
    @api.doc(body=user_fields)
    def post(self):
        schema = UserLoginSchema()
        data = schema.load(request.json)

        username = data['username']
        passw = data['password']

        user = User.query.filter_by(username=username).first()

        if not user or not bcrypt.hashpw(passw.encode(), bcrypt.gensalt()):
            return {'error': 'invalid username or password'}, 404

        
        token = create_access_token(identity=user.id)
        return {
            'user': UserSchema().dump(user),
            'token': token
        }, 200


api.add_resource(UserList, '')
api.add_resource(UserId, '/<int:id>')
api.add_resource(UserLogin, '/login')