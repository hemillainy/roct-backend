from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from roct.models import User
import requests
import json
import uuid


from roct import db
from roct.models import Payment

payments = Blueprint('payments', __name__)

@payments.route('generate_qr_code', methods=['POST'])
# @jwt_required
def generate_qr_code():
    data = request.get_json()
    user = User.query.get(data['buyer']).serialize()
    referenceId = str(uuid.uuid4())


    payload = {
        'referenceId': referenceId,
        'callbackUrl': 'https://roct-api.herokuapp.com/payment_callback',
        'value': data['value'],
        'buyer': {
            'firstName': user['name'],
            'lastName': '',
            'document': user['cpf'],
            'email': user['email'],
            'phone': user['phone']
        },
        'returnUrl': ''
    }

    headers = {'x-picpay-token': '62d554b7-972a-4440-9f01-d31b1d1f6058', 'Content-Type': 'application/json'}
    r = requests.post('https://appws.picpay.com/ecommerce/public/payments', data=json.dumps(payload), headers=headers)    

    payment = Payment(r.json()['paymentUrl'], r.json()['qrcode']['base64'], referenceId)
    
    db.session.add(payment)
    db.session.commit()

    return jsonify({
        'url': r.json()['paymentUrl'],
        'qrCode': r.json()['qrcode']['base64']
    })


@payments.route('payment_callback', methods=['POST'])
def payment_callback():
    print("callback")
    return jsonify({})
