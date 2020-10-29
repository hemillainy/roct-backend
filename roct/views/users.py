from flask import Blueprint, request, abort
from roct import db
from roct.models import User

users_resource = Blueprint('users', __name__)


def check_password(pwd):
    if pwd['password'] != pwd['confirm_password']:
        abort(412)


@users_resource.route('', methods=['POST'])
def create():
    data = request.get_json()

    check_password(data['pwd'])
    data.pop('pwd')

    user = User(**data)
    db.session.add(user)
    db.session.commit()

    return user.serialize(), 201


@users_resource.route('<id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    user = User.query.get_or_404(id)

    user.query.update(data)
    db.session.commit()

    return user.serialize()


@users_resource.route('<id>', methods=['GET'])
def get(id):
    user = User.query.get_or_404(id)

    return user.serialize()
