from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, ValidationError, BooleanField, TextAreaField, SelectField, RadioField
from wtforms.validators import Required
from ..models import User

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class BlogsForm(FlaskForm):
    title = TextAreaField('Title')
    texto = TextAreaField('Blogs')
    submit = SubmitField()