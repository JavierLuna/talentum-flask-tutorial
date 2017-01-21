import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from app import create_app, db
from app.models import User, Post, Comment, Tag

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
	def clear():
		[print() for _ in range(20)]

	def db_add(o):
		db.session.add(o)
		db.session.commit()

	def generate_fake():
		User.generate_fake()
		Post.generate_fake()
		Comment.generate_fake()
		Tag.generate_fake()

	return dict(app=app, db=db, User=User, Post=Post, Comment=Comment, Tag=Tag, clear=clear, db_add=db_add,
	            generate_fake=generate_fake)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()