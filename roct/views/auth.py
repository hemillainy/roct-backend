from flask import Blueprint, request, jsonify, make_response
from roct import db
from flask_jwt_extended import (JWTManager, create_access_token)
from flask_bcrypt import Bcrypt
from dataclasses import dataclass
import base64

from roct.models import User

auth = Blueprint('auth', __name__)

jwt = JWTManager()
bcrypt = Bcrypt()

@dataclass
class AuthUser:
    def __init__(self, id, email):
        self.id = id
        self.email = email


@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    email = data['email']
    password = data['password']

    user = User.query.filter_by(email=email).first()
    print(bcrypt.check_password_hash(user.password, password))
    if user is None or not bcrypt.check_password_hash(user.password, password):
        return jsonify({ 'msg': 'Bad credentials' }), 401

    auth_user = AuthUser(user.id, user.email)

    return make_response(jsonify({
        'token': create_access_token(auth_user)
    }))