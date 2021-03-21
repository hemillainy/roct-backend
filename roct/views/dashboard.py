from flask import Blueprint, request, jsonify
from roct import db
from roct.models import User, Purchase, Announcement
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_bcrypt import Bcrypt
from roct.utils import check_user_is_super

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/alive', methods=['GET'])
def alive():
  return "dashboard alive"

@dashboard.route('/metrics', methods=['GET'])
@jwt_required
@check_user_is_super
def get_metrics(): 
    users = User.query.all()
    # import pdb; pdb.set_trace()
    salesmans = [e for e in users if e.isSalesman]
    purchases = Purchase.query.all()
    total_purchases_value = 0
    for e in purchases:
      temp = e.get_announcement
      total_purchases_value += temp['price']
    items = Announcement.query.all()
    total_users = len(users)
    total_salesman = len(salesmans)
    total_purchases = len(purchases)
    purchases_value = total_purchases_value
    total_items= len(items)
    metrics = {
      'total_users': total_users,
      'total_salesman': total_salesman,
      'total_purchases': total_purchases,
      'purchases_value': purchases_value,
      'total_items': total_items,
    }

    return metrics
    

@dashboard.route('/limit-user/<id>', methods=['PUT'])
@jwt_required
@check_user_is_super
def limit_user(id):
    print(id)
    user = User.query.get_or_404(id)
    setattr(user, 'limited', True)
    db.session.commit()
    return user.serialize()
    