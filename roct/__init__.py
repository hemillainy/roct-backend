import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

APP_ROOT = os.path.join(os.path.dirname('__file__'), '..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Blueprints
from roct.views import auth, jwt, announcements, commands, users_resource

jwt.init_app(app)

app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(announcements, url_prefix="/announcements")
app.register_blueprint(commands, url_prefix="/commands")
app.register_blueprint(users_resource, url_prefix="/users")
