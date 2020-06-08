from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length


class GuideForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[DataRequired(),
        Length(min=3, max=20)])
    surname = StringField(
        'Surname',
        validators=[DataRequired(),
        Length(min=3, max=20)])
    phone = StringField(
        'Phone',
        validators=[DataRequired(),
        Length(min=9, max=15)])
    email = StringField(
        'Email',
        validators=[DataRequired()])
    image_file = StringField(
        'image_file')



class TravelForm(FlaskForm):
    guide_id = StringField(
        'guide_id',
        validators=[DataRequired()])
    title = StringField(
        'title',
        validators=[DataRequired()])
    content = TextAreaField(
        'content',
        validators=[DataRequired()])
