from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired, Length



class PostCreationForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired(), Length(1, 200)])
	body = TextAreaField('Body', validators=[DataRequired(), Length(1, 999)])
	tags = SelectMultipleField('Tags')
	submit = SubmitField('Post')


class TagCreationForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired(), Length(1, 100)])
	submit = SubmitField('Create tag')

class CommentCreationForm(FlaskForm):
	content = TextAreaField('', validators=[DataRequired(), Length(1, 900)])
	submit = SubmitField('Submit')