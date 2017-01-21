from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config


db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name='default'):
	app = Flask(__name__, static_folder='./static')
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	# Inicializar plugins aquí
	db.init_app(app)
	bootstrap.init_app(app)

	# Registrar blueprints aquí
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app