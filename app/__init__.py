from flask import Flask
from config import config



def create_app(config_name='default'):
	app = Flask(__name__, static_folder='./static')
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	# Inicializar plugins aquí

	# Registrar blueprints aquí
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app