from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from functools import wraps
from roct.models import User


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

def check_user_is_super(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        user = get_jwt_identity()
        user_ = User.query.get_or_404(user['id'])
        if not user_.isSuper:
            return jsonify(msg='Forbidden'), 403
        else:
            return fn(*args, **kwargs)

    return wrapper