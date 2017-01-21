from flask import redirect, request, url_for, flash, render_template
from flask_login import login_user, login_required, logout_user

from app import db
from . import auth
from .forms import LoginForm, RegistrationForm
from ..models import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			return redirect(request.args.get('next') or url_for('main.frontpage'))
		flash('Invalid username or password')
	return render_template('auth/login.html', form=form, blog_title="Login", blog_subtitle="")


@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out')
	return redirect(url_for('main.frontpage'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(email=form.email.data, username=form.username.data, password=form.password.data)
		user.generate_gravatar()
		db.session.add(user)
		flash("You can now login")
		return redirect(url_for('auth.login'))
	return render_template('auth/registration.html', form=form, blog_title="Register", blog_subtitle="Come join us!")
