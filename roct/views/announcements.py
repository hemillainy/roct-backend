from flask import Blueprint, request, jsonify
from roct import db

from roct.models import Announcement

announcements = Blueprint('announcements', __name__)


@announcements.route('check', methods=['GET'])
def check():
    return "Hello World"


@announcements.route('', methods=['GET'])
def get_all():
    return jsonify({
        'data': [e.serialize for e in Announcement.query.all()]
    })


@announcements.route('search/<game_search>/<server_search>/<name_search>', methods=['GET'])
def search_in_server(game_search, server_search, name_search):
    find = Announcement.query.filter(
        Announcement.game.is_(game_search),
        Announcement.server.is_(server_search),
        Announcement.name.contains(name_search)
    ).all()
    return jsonify({
        'data': [e.serialize for e in find]
    })


@announcements.route('search/<game_search>/<name_search>', methods=['GET'])
def search_in_game(game_search, name_search):
    find = Announcement.query.filter(
        Announcement.game.is_(game_search),
        Announcement.name.contains(name_search)
    ).all()
    return jsonify({
        'data': [e.serialize for e in find]
    })


@announcements.route('<uuid>', methods=['GET'])
def get_one(uuid):
    announcement = Announcement.query.get(uuid)
    return jsonify(announcement.serialize)


@announcements.route('search/<var>', methods=['GET'])
def search(var):
    find = Announcement.query.filter(Announcement.name.contains(var)).all()
    return jsonify({
        'data': [e.serialize for e in find]
    })


@announcements.route('add', methods=['POST'])
def create():
    print("\n\n\n")
    print(request.get_json())
    print("\n\n\n")
    announcement = Announcement(**request.get_json())
    db.session.add(announcement)
    db.session.commit()
    return jsonify(announcement.serialize)


# @announcements.route('edit/<uuid>', methods=['POST'])
# def edit(uuid):
#     announcement = Announcement.query.get(uuid)
#     print("editing")
#     return jsonify(announcement.serialize)
