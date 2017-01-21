import datetime
import hashlib

from slugify import slugify
from werkzeug.security import generate_password_hash, check_password_hash

from . import db

post_has_tags = db.Table('post_has_tags',
                         db.Column('post_id', db.Integer, db.ForeignKey('posts.id')),
                         db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
                         )


class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True, nullable=False)
	photo = db.Column(db.String(200))
	email = db.Column(db.String(255), unique=True, index=True, nullable=False)
	password_hash = db.Column(db.Text(), nullable=False)

	# Relaciones
	posts = db.relationship('Post', backref='user', lazy='dynamic')
	comments = db.relationship('Comment', backref='user', lazy='dynamic')

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	def generate_gravatar(self):
		self.photo = "https://www.gravatar.com/avatar/" + hashlib.md5(
			self.email.lower().encode('utf-8')).hexdigest() + "?size=60"

	def __repr__(self):
		return "<User " + self.username + " >"


class Post(db.Model):
	__tablename__ = 'posts'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False, unique=True)
	body = db.Column(db.Text(), nullable=False)
	slug = db.Column(db.String(200))

	created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	edited_on = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

	# Relaciones

	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	comments = db.relationship('Comment', backref='post', lazy='dynamic')
	tags = db.relationship('Tag', secondary=post_has_tags,
	                       backref=db.backref('posts', lazy='dynamic'), lazy='dynamic')

	def generate_slug(self):
		self.slug = slugify(self.title)

	def __repr__(self):
		return "<Post " + self.title + " >"


class Comment(db.Model):
	__tablename__ = 'comments'

	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.Text(), nullable=False)
	posted_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)

	# Relaciones
	post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __repr__(self):
		return "<Comment " + self.body + " >"


class Tag(db.Model):
	__tablename__ = 'tags'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False, unique=True)
	slug = db.Column(db.String(200))

	def generate_slug(self):
		self.slug = slugify(self.name)

	def __repr__(self):
		return "<Tag " + self.name + ">"
