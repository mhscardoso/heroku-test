from flask import Blueprint
from flask_restx import Api

from app.user.controller import api as user_ns
from app.messages.controller import api as messages_ns

api_bp = Blueprint('api', __name__)

authorizations = {
    'apikey' : {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
    }
}

api = Api(api_bp, title='Heroku Test', description='Rest API - Heroku Test', authorizations=authorizations, security='apikey')

# Add everything!!!
api.add_namespace(user_ns)
api.add_namespace(messages_ns)