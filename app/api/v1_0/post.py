from flask import abort
from flask import jsonify
from flask import request, current_app
from flask import url_for
from sqlalchemy.exc import IntegrityError

from . import json
from app import db
from app.models import Post, User
from . import api1_0
from .. import api_auth


@api1_0.route("/posts", methods=['GET'])
@json
def list_posts():
	page = request.args.get('page', 1, type=int)
	pagination = Post.query.order_by(Post.created_on.desc()).paginate(
		page, per_page=current_app.config['RESULTS_PER_API_CALL'], error_out=False
	)
	response = {
		'next': url_for('api1_0.list_posts', page=pagination.next_num, _external=True) if pagination.has_next else "",
		'prev': url_for('api1_0.list_posts', page=pagination.prev_num, _external=True) if pagination.has_prev else "",
		'items': [post.to_json() for post in pagination.items]
	}
	return response


@api1_0.route("/posts", methods=['POST'])
@api_auth.login_required
def create_post():
	post = Post(title=request.form['title'], body=request.form['body'],
	            user=User.query.filter_by(username=api_auth.username()).first())
	post.generate_slug()
	try:
		db.session.add(post)
		db.session.commit()
	except IntegrityError:
		db.session.rollback()
		abort(409)
	response = jsonify({'id': post.id})
	response.status_code = 201
	response.headers['Location'] = url_for('api1_0.detail_post', postid=post.id)
	return response


@api1_0.route('/posts/<int:postid>', methods=['GET'])
@json
def detail_post(postid):
	post = Post.query.get_or_404(postid)
	return post


@api1_0.route('/posts/<int:postid>', methods=['PUT'])
@api_auth.login_required
@json
def update_post(postid):
	post = Post.query.get_or_404(postid)
	post.title = request.form['title']
	post.body = request.form['body']
	post.generate_slug()
	try:
		db.session.add(post)
		db.session.commit()
	except IntegrityError:
		db.session.rollback()
		abort(409)
	return post


@api1_0.route('/posts/<int:postid>', methods=['DELETE'])
@api_auth.login_required
def delete_post(postid):
	post = Post.query.get_or_404(postid)
	db.session.delete(post)
	db.session.commit()
	return ('', 204)
