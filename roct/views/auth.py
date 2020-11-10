from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import (JWTManager, create_access_token)
from flask_bcrypt import Bcrypt
from dataclasses import dataclass
import datetime
from roct.models import User

auth = Blueprint('auth', __name__)

jwt = JWTManager()
bcrypt = Bcrypt()


@dataclass
class AuthUser:
    def __init__(self, id, email):
        self.id = id
        self.email = email

    @jwt.user_identity_loader
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email
        }


def create_response_user_and_token(user):
    auth_user = AuthUser(user.id, user.email)

    expires = datetime.timedelta(days=1)

    return make_response(jsonify({
            'token': create_access_token(auth_user, expires_delta=expires),
            'user': user.serialize()
        })
        )


@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data['email']
    password = data['password']

    user = User.query.filter_by(email=email).first()
    if user is None or not bcrypt.check_password_hash(user.password, password):
        return jsonify({'msg': 'Bad credentials'}), 401

    return create_response_user_and_token(user)

