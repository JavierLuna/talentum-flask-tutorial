from flask_httpauth import HTTPBasicAuth

from ..models import User

api_auth = HTTPBasicAuth()

@api_auth.verify_password
def verify_pw(username, password):
	user = User.query.filter_by(username=username).first()
	if user is not None:
		return user.verify_password(password)
	return False

from .v1_0 import *