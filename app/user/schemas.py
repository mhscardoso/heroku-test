from app.extensions import ma
from app.user.model import User

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
        ordered = True
    
    id = ma.Integer(dump_only=True)
    username = ma.String(required=True)
    password = ma.String(load_only=True, required=True)


class UserLoginSchema(ma.Schema):
    username = ma.String(required=True)
    password = ma.String(required=True, load_only=True)