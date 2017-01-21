from flask import render_template

from . import main
from ..models import Post, Tag


@main.route('/')
def frontpage():
	return render_template("main/frontpage.html", posts=Post.query.all(), tags=Tag.query.all())


@main.route('/post/<post_slug>')
def post_detail(post_slug):
	post = Post.query.filter_by(slug=post_slug).first_or_404()
	return render_template('main/postdetail.html', post=post, tags=Tag.query.all())


@main.route('/tag/<tag_slug>')
def tagged_posts(tag_slug):
	tag = Tag.query.filter_by(slug=tag_slug).first_or_404()
	return render_template("main/frontpage.html", posts=tag.posts.all(), tags=Tag.query.all(),
	                       blog_title="Tagged as " + tag.name, blog_subtitle="",
	                       title="Tagged as " + tag.name)
