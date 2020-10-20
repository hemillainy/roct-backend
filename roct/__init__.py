import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Blueprints
from roct.views import auth, users_resource
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(users_resource, url_prefix="/users")

db.create_all()
