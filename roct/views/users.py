from flask import Blueprint, request, jsonify
from roct import db
from roct.models import User
from flask_jwt_extended import jwt_required
from roct.utils import check_user_is_same
from flask_bcrypt import Bcrypt
from .auth import create_response_user_and_token

users_resource = Blueprint('users', __name__)
bcrypt = Bcrypt()


@users_resource.route('', methods=['POST'])
def create():
    data = request.get_json()

    user = User(**data)

    db.session.add(user)
    db.session.commit()

    return create_response_user_and_token(user), 201


@users_resource.route('<id>', methods=['PUT'])
@jwt_required
@check_user_is_same
def update(id):
    data = request.get_json()
    blocked_fields = {"password", 'id'}

    user = User.query.get_or_404(id)

    if user.isSalesman:
        blocked_fields.add('isSalesman')

    for key in data:
        if key not in blocked_fields:
            setattr(user, key, data[key])

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

    if not bcrypt.check_password_hash(user.password, data['oldPassword']):
        return jsonify({'msg': 'Bad credentials'}), 401

    new_value = bcrypt.generate_password_hash(data['newPassword']).decode()

    setattr(user, 'password', new_value)
    db.session.commit()

    return user.serialize()
