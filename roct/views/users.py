from flask import Blueprint, request, jsonify
from roct import db
from roct.models import User
from flask_jwt_extended import jwt_required
from roct.utils import check_user_is_same, check_user_is_super, paginate
from flask_bcrypt import Bcrypt
from .auth import create_response_user_and_tokens

users_resource = Blueprint('users', __name__)
bcrypt = Bcrypt()


@users_resource.route('', methods=['POST'])
def create():
    data = request.get_json()
    data['isSuper'] = False
    data['limited'] = False

    user = User(**data)

    db.session.add(user)
    db.session.commit()

    return create_response_user_and_tokens(user), 201


@users_resource.route('<id>', methods=['PUT'])
@jwt_required
@check_user_is_same
def update(id):
    data = request.get_json()
    blocked_fields = {"password", 'id', "isSuper"}

    user = User.query.get_or_404(id)

    if user.isSalesman:
        blocked_fields.add('isSalesman')

    for key in data:
        if key not in blocked_fields:
            setattr(user, key, data[key])

    db.session.commit()

    return user.serialize()

def get_filters(): 
    return {
        "name": request.args.get('name'),
        "cpf": request.args.get('cpf'),
        "email": request.args.get('email'),
        "limited": request.args.get('limited'),
        "page": request.args.get('page'),
        "per_page": request.args.get('per_page'),
        "isSalesman": request.args.get('isSalesman'),
    }

@users_resource.route('', methods=['GET'])
@jwt_required
@check_user_is_super
def get_all():
    queries = get_filters()
    filters = []
    page = 1
    per_page = 10

    if queries['name']:
        name = "%{}%".format(request.args.get('name'))
        filters.append(User.name.like(name))
    if queries['cpf']:
        cpf = "%{}%".format(request.args.get('cpf'))
        filters.append(User.name.like(cpf))
    if queries['email']:
        email = "%{}%".format(request.args.get('email'))
        filters.append(User.name.like(email))
    if queries['limited']:
        limited = request.args.get('limited')
        limited = True if limited == "true" else False
        filters.append(User.limited == limited)
    if queries['isSalesman']:
        isSalesman = request.args.get('isSalesman')
        isSalesman = True if isSalesman == "true" else False
        filters.append(User.isSalesman == isSalesman)
    if queries['page']:
        page = int(queries['page'])
    if queries['per_page']:
        per_page = int(queries['per_page'])

    
    users = User.query.filter(*filters)

    return paginate(users, page, per_page)

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
