from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import (JWTManager, create_access_token, get_jwt_identity, jwt_required, create_refresh_token, jwt_refresh_token_required)
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



def create_response_user_and_tokens(user):
    auth_user = AuthUser(user.id, user.email)
    print("USSSSSER", auth_user.serialize())

    return make_response(jsonify({
        'token': generate_access_token(auth_user),
        'refresh_token': create_refresh_token(auth_user),
        'user': user.serialize()
    })
    )


def generate_access_token(auth_user):
    expires = datetime.timedelta(days=1)

    access_token = create_access_token(auth_user, expires_delta=expires)
    return access_token


@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data['email']
    password = data['password']

    user = User.query.filter_by(email=email).first()

    if user is None or not bcrypt.check_password_hash(user.password, password):
        return jsonify({'msg': 'Bad credentials'}), 401

    return create_response_user_and_tokens(user)


@auth.route('/refresh_token', methods=['GET'])
@jwt_refresh_token_required
def refresh_token():
    user = get_jwt_identity()
    auth_user = AuthUser(user["id"], user["email"])

    token = generate_access_token(auth_user)
    return make_response(jsonify({
        'token': token
    }))
