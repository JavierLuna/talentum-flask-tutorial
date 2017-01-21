import datetime
import hashlib

from slugify import slugify
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import db, login_manager

post_has_tags = db.Table('post_has_tags',
                         db.Column('post_id', db.Integer, db.ForeignKey('posts.id')),
                         db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
                         )

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(UserMixin, db.Model):
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

	@staticmethod
	def generate_fake(count=100):
		from sqlalchemy.exc import IntegrityError
		from random import seed
		import forgery_py

		seed()
		for _ in range(count):
			u = User(username=forgery_py.internet.user_name(with_num=True),
			         email=forgery_py.internet.email_address(),
			         password=forgery_py.lorem_ipsum.word())
			u.generate_gravatar()

			db.session.add(u)
			try:
				db.session.commit()
			except IntegrityError:
				db.session.rollback()



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

	@staticmethod
	def generate_fake(count=100):
		from random import seed, randint
		from sqlalchemy.exc import IntegrityError
		import forgery_py

		seed()
		user_count = User.query.count()
		for _ in range(count):
			u = User.query.offset(randint(0, user_count - 1)).first()
			p = Post(title=forgery_py.lorem_ipsum.words(3),
			         body=forgery_py.lorem_ipsum.sentences(randint(1, 3)),
			         user=u)

			p.generate_slug()

			db.session.add(p)
			try:
				db.session.commit()
			except IntegrityError:
				db.session.rollback()

	def to_json(self):
		return {'id': self.id,
		        'title': self.title,
		        'body': self.body,
		        'slug': self.slug,
		        'created_on': str(self.created_on),
		        'edited_on': str(self.edited_on),
		        'user': self.user.username,
		        'tags': [tag.to_json() for tag in self.tags.all()],
		        'comments': [comment.to_json() for comment in self.comments.all()]}

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

	@staticmethod
	def generate_fake(count=100):
		from random import seed, randint
		from sqlalchemy.exc import IntegrityError
		import forgery_py

		seed()
		post_count = Post.query.count()
		user_count = User.query.count()
		for _ in range(count):
			p = Post.query.offset(randint(0, post_count - 1)).first()
			u = User.query.offset(randint(0, user_count - 1)).first()
			c = Comment(body=forgery_py.lorem_ipsum.words(), user=u, post=p)
			db.session.add(c)
			try:
				db.session.commit()
			except IntegrityError:
				db.session.rollback()

	def to_json(self):
		return {'id': self.id,
		        'body': self.body,
		        'posted_on': str(self.posted_on),
		        'post_id': self.post_id,
		        'user': self.user.username}

	def __repr__(self):
		return "<Comment " + self.body + " >"


class Tag(db.Model):
	__tablename__ = 'tags'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False, unique=True)
	slug = db.Column(db.String(200))

	def generate_slug(self):
		self.slug = slugify(self.name)

	@staticmethod
	def generate_fake(count=6):
		from random import seed, randint
		from sqlalchemy.exc import IntegrityError
		import forgery_py

		seed()
		post_count = Post.query.count()
		for _ in range(count):
			p = Post.query.offset(randint(0, post_count - 1)).first()
			t = Tag(name=forgery_py.lorem_ipsum.word())

			t.generate_slug()
			t.posts.append(p)

			db.session.add(t)
			try:
				db.session.commit()
			except IntegrityError:
				db.session.rollback()

	def to_json(self):
		return {'id': self.id,
		        'name': self.name,
		        'slug': self.slug}

	def __repr__(self):
		return "<Tag " + self.name + ">"
