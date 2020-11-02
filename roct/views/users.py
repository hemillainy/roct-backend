from flask import Blueprint, request
from roct import db
from roct.models import User
from flask_jwt_extended import jwt_required
from roct.utils import check_user_is_same

users_resource = Blueprint('users', __name__)


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
