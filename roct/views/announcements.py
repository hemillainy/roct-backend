from flask import Blueprint, request, jsonify
from roct import db

from roct.models import Announcement

announcements = Blueprint('announcements', __name__)

@announcements.route('check', methods=['GET'])
def check():
    return "Hello World"

@announcements.route('add', methods=['POST'])
def create():
    print("\n\n\n")
    print(request.get_json())
    print("\n\n\n")
    announcement = Announcement(**request.get_json())
    db.session.add(announcement)
    db.session.commit()
    return jsonify(announcement.serialize)

@announcements.route('edit/<uuid>', methods=['POST'])
def edit(uuid):
    announcement = Announcement.query.get(uuid)
    print("editando")
    return jsonify(announcement.serialize)