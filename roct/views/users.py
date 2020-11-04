from flask import Blueprint, request
from roct import db
from roct.models import User
from flask_jwt_extended import jwt_required
from roct.utils import check_user_is_same
from flask_bcrypt import Bcrypt

users_resource = Blueprint('users', __name__)
bcrypt = Bcrypt()


@users_resource.route('', methods=['POST'])
def create():
    data = request.get_json()

    user = User(**data)
    db.session.add(user)
    db.session.commit()

    return user.serialize(), 201


@users_resource.route('<id>', methods=['PUT'])
@jwt_required
@check_user_is_same
def update(id):
    data = request.get_json()

    if 'password' in data:
        del data['password']

    user = User.query.get_or_404(id)

    user.query.update(data)
    db.session.commit()

    return user.serialize()


@users_resource.route('<id>', methods=['GET'])
@jwt_required
@check_user_is_same
def get(id):
    user = User.query.get_or_404(id)

    return user.serialize()


@users_resource.route('<id>/changePassword', methods=['PUT'])
@jwt_required
@check_user_is_same
def change_password(id):
    data = request.get_json()
    user = User.query.get_or_404(id)

    new_values = {
        "password": bcrypt.generate_password_hash(data['password']).decode()
    }

    user.query.update(new_values)
    db.session.commit()

    return user.serialize()
