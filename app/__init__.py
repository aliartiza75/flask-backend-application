from app.datetime_api.routes import mod
from flask import Flask, Blueprint
from flask_api import FlaskAPI
app = Flask(__name__)

# registering application
app.register_blueprint(mod, uri_prefix='/datetime_api')
