import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

project_folder = os.path.expanduser('~/roct-backend')
load_dotenv(os.path.join(project_folder, '.env'))


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
