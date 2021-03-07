from flask import Blueprint, request, jsonify, abort
from roct import db
from flask_jwt_extended import jwt_required, get_jwt_identity

from roct.models import Purchase, Announcement
from roct.models.enums import PurchaseStatusEnum

purchases = Blueprint('purchases', __name__)


def paginate(query, page, per_page):
    page = query.paginate(page=page, per_page=per_page)
    items = [e.serialize for e in page.items]
    info = {
        "page": page.page,
        "per_page": page.per_page,
        "total": page.total
    }

    return jsonify({
        'data': items,
        "info": info
    })


@purchases.route('add', methods=['POST'])
@jwt_required
def add():
    purchase = Purchase(**request.get_json())

    announcement = Announcement.query.get(purchase.announcement_uuid)
    setattr(announcement, 'available', False)

    db.session.add(purchase)
    db.session.commit()
    return jsonify(purchase.serialize)


@purchases.route('update_status', methods=['POST'])
@jwt_required
def update_status():
    data = request.get_json()
    purchase_id = data['id']
    purchase = Purchase.query.get(purchase_id)
    status = purchase.status
    if status.name == PurchaseStatusEnum.initiated.name:
        new_status = PurchaseStatusEnum.paid
    elif status.name == PurchaseStatusEnum.paid.name:
        new_status = PurchaseStatusEnum.delivered
    else:
        new_status = PurchaseStatusEnum.finished
    setattr(purchase, 'status', new_status)
    db.session.commit()
    return jsonify(purchase.serialize)


@purchases.route('sales', methods=['POST'])
@jwt_required
def get_sales():
    data = request.get_json()
    salesman_uuid = data['id']
    page = data['page']
    per_page = data['per_page']

    salesman_ann = Purchase.query.filter_by(salesman_uuid=salesman_uuid)
    return paginate(salesman_ann, page=page, per_page=per_page)


@purchases.route('purchases', methods=['POST'])
@jwt_required
def get_purchases():
    data = request.get_json()
    buyer_uuid = data['id']
    page = data['page']
    per_page = data['per_page']

    salesman_ann = Purchase.query.filter_by(buyer_uuid=buyer_uuid)
    return paginate(salesman_ann, page=page, per_page=per_page)


@purchases.route('<uuid>/confirmDelivery', methods=['PUT'])
@jwt_required
def confirm_delivery(uuid):
    user = get_jwt_identity()
    purchase = Purchase.query.get_or_404(uuid)
    is_salesman = purchase.salesman_uuid == user['id']

    if user['id'] != purchase.salesman_uuid and user['id'] != purchase.buyer_uuid:
        return jsonify(mgs='Forbidden'), 403
    if purchase.status == PurchaseStatusEnum.finished.value:
        return jsonify(mgs='Confirmation not available!'), 409

    if is_salesman:
        purchase.salesman_delivery_confirmation = True
    else:
        purchase.buyer_delivery_confirmation = True
    
    #Se o comprador confirmar recebimento, a compra já deve ir para finished
    #Se o vendedor confirmar entrega, deve ir para delivered
    if purchase.salesman_delivery_confirmation and purchase.buyer_delivery_confirmation:
        purchase.status = PurchaseStatusEnum.finished
    elif purchase.buyer_delivery_confirmation:
        purchase.status = PurchaseStatusEnum.finished
    elif purchase.salesman_delivery_confirmation:
        purchase.status = PurchaseStatusEnum.delivered

    db.session.commit()

    return purchase.serialize

