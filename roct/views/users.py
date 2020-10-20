from flask import Blueprint, request, jsonify
from roct import db
from roct.models import User

users_resource = Blueprint('users', __name__)


@users_resource.route('', methods=['POST'])
def create():
    data = request.get_json()
    user = User(**data)
    db.session.add(user)
    db.session.commit()

    return user.serialize()


@users_resource.route('<uuid>', methods=['PUT'])
def update(uuid):
    data = request.get_json()
    user = User.query.get_or_404(uuid)

    user.query.update(data)
    db.session.commit()

    return user.serialize()


@users_resource.route('<uuid>', methods=['GET'])
def get(uuid):
    user = User.query.get_or_404(uuid)

    return user.serialize()
