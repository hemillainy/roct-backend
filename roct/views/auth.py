from flask import Blueprint
from roct import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    return 'Login'


@auth.route('/signup', methods=['POST'])
def signup():
    return 'Signup'


