from flask import Blueprint, request, jsonify
from roct import db

commands = Blueprint('commands', __name__)


@commands.route('check', methods=['GET'])
def check():
    return "Hello World from commands"


@commands.route('restart', methods=['POST'])
def restart():
    db.drop_all()
    db.create_all()
    return jsonify({
        'data': 'Database restarted.'
    })

