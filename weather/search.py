from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class Search(FlaskForm):
	city = StringField('City', validators=[DataRequired()])
	time = HiddenField('Time')