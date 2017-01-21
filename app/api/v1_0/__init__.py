from functools import wraps

from flask import Blueprint, jsonify

api1_0 = Blueprint('api1_0', __name__)

@api1_0.errorhandler(409)
def error_409(e):
	return jsonify({'error': 'Aborted, a conflict may had happened'}), 409

@api1_0.errorhandler(400)
def error_keyerror(e):
	return jsonify({'error': 'Expected one or more parameters to the call'}), 400

@api1_0.errorhandler(401)
def error_keyerror(e):
	return jsonify({'error': 'Unauthorized access'}), 401

def json(f):
	@wraps(f)
	def wrapped(*args, **kwargs):
		rv = f(*args, **kwargs)
		if not isinstance(rv, dict):
			rv = rv.to_json()
		return jsonify(rv)
	return wrapped

from . import post
