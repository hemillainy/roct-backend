from flask import jsonify, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps


def check_password(pwd):
    if pwd['password'] != pwd['confirm_password']:
        abort(412)


def check_user_is_same(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        user = get_jwt_identity()
        id_required = int(kwargs['id'])

        if user['id'] != id_required:
            return jsonify(msg='Forbidden'), 403
        else:
            return fn(*args, **kwargs)

    return wrapper
