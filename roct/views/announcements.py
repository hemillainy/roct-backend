from flask import Blueprint, request, jsonify
from roct import db, mail
import re
from flask_jwt_extended import jwt_required, get_jwt_identity

from roct.models import Announcement, User
from roct.models.enums import AnnouncementStatusEnum, AnnouncementTypeEnum
from flask_mail import Message
from roct.utils import paginate, get_limited_users_ids

announcements = Blueprint('announcements', __name__)



@announcements.route('check', methods=['GET'])
def check():
    return "Hello World"


@announcements.route('', methods=['POST'])
def get_all():
    data = request.get_json()
    limiteds = get_limited_users_ids()
    page = data['page']
    per_page = data['per_page']

    find = Announcement.query.filter_by(available=True).filter(Announcement.salesman_uuid.notin_(limiteds))
    return paginate(find, page=page, per_page=per_page)


@announcements.route('<uuid>', methods=['GET'])
def get_one(uuid):
    announcement = Announcement.query.get(uuid)
    return jsonify(announcement.serialize())

@announcements.route('<uuid>', methods=['DELETE'])
@jwt_required
def delete(uuid):
    announcement = Announcement.query.get(uuid)
    user = get_jwt_identity()

    if not announcement: 
        return jsonify({'msg': 'Announcement not found!'}), 404
    
    salesman_id = announcement.salesman_uuid

    if user["id"] != salesman_id:
        return jsonify({'msg': 'Forbidden!'}), 403
    elif not announcement.available:
        return jsonify({'msg': 'Announcement cannot be deleted!'}), 409
    
    db.session.delete(announcement)
    db.session.commit()

    return jsonify({'msg': 'Announcement deleted!'}), 200

def is_valid_parameter(parameter):
    return parameter and type(parameter) == str


def filter_by_item(find, var):
    find = find.filter(Announcement.name.contains(var))
    return find


@announcements.route('search', methods=['POST'])
def search():
    data = request.get_json()
    game_search = data['game'],
    server_search = data['server'],
    name_search = data['item']
    type_search = data['type_']

    page = data['page']
    per_page = data['per_page']

    find = Announcement.query
    if is_valid_parameter(game_search):
        print("FILTER BY GAME", game_search)
        find = find.filter_by(game=game_search)
    if is_valid_parameter(server_search):
        print("FILTER BY SERVER", server_search)
        find = find.filter_by(server=server_search)
    if is_valid_parameter(type_search):
        print("FILTER BY TYPE", type_search)
        find = find.filter_by(type_=type_search)
    if is_valid_parameter(name_search):
        print("FILTER BY NAME", name_search)
        find = filter_by_item(find, name_search)

    limiteds = get_limited_users_ids()
    find = find.filter_by(available=True).filter(Announcement.salesman_uuid.notin_(limiteds))
    return paginate(find, page=page, per_page=per_page)


@announcements.route('add', methods=['POST'])
@jwt_required
def create():
    user = get_jwt_identity()
    user_ = User.query.get_or_404(user['id'])
    if user_.limited:
      return jsonify(msg='Usuário limitado. Não pode criar anuncio'), 400
    announcement = Announcement(**request.get_json())
    db.session.add(announcement)
    db.session.commit()
    return jsonify(announcement.serialize())


@announcements.route('status', methods=['GET'])
def get_status():
    status = [e.name for e in list(AnnouncementStatusEnum)]
    return jsonify(status)


@announcements.route('types', methods=['GET'])
def get_types():
    types = [e.name for e in list(AnnouncementTypeEnum)]
    return jsonify(types)


@announcements.route('games', methods=['GET'])
def get_games():
    games = list(set([e.game for e in Announcement.query.all()]))
    games.append('WYD')
    games = sorted(list(set(games)))
    return jsonify(games)


@announcements.route('servers', methods=['GET'])
def get_servers():
    servers = list(set([e.server for e in Announcement.query.all()]))
    servers.append('Test')
    servers = sorted(list(set(servers)))
    return jsonify(servers)


@announcements.route('salesman/<salesman_uuid>', methods=['POST'])
@jwt_required
def get_salesman_ann(salesman_uuid):
    data = request.get_json()
    page = data['page']
    per_page = data['per_page']

    salesman_ann = Announcement.query.filter_by(salesman_uuid=salesman_uuid)
    return paginate(salesman_ann, page=page, per_page=per_page)


# @announcements.route('edit/<uuid>', methods=['POST'])
# def edit(uuid):
#     announcement = Announcement.query.get(uuid)
#     print("editing")
#     return jsonify(announcement.serialize)

def send_notification_email(email):
    msg = Message("Anúncio Vendido", sender="roct.proj1@gmail.com", recipients = [email])
    msg.body = ""
    mail.send(msg)
    return "sent"
