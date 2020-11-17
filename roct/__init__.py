import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_mail import Mail

project_folder = os.path.expanduser('~/roct-backend')
load_dotenv(os.path.join(project_folder, '.env'))


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'roct.proj1@gmail.com'
app.config['MAIL_PASSWORD'] = 'roct1234'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)


# Blueprints
from roct.views import auth, jwt, announcements, commands, users_resource

jwt.init_app(app)

app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(announcements, url_prefix="/announcements")
app.register_blueprint(commands, url_prefix="/commands")
app.register_blueprint(users_resource, url_prefix="/users")
