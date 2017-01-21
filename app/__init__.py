from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config


db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name='default'):
	app = Flask(__name__, static_folder='./static')
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	# Inicializar plugins aquí
	db.init_app(app)
	bootstrap.init_app(app)
	login_manager.init_app(app)

	# Registrar blueprints aquí
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint, url_prefix='/auth')

	return app