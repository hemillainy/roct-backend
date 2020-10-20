import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
print(os.getenv('DB_URI'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Blueprints
from roct.views import auth, announcements, commands, users_resource
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(announcements, url_prefix="/announcements")
app.register_blueprint(commands, url_prefix="/commands")
app.register_blueprint(users_resource, url_prefix="/users")

db.create_all()
