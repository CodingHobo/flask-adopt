"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, Email

# {{ form.hidden_tag() }}
# pet name, species, photo url, age, notes: url path /add
# add alink to this from the homepage


class AddPetForm(FlaskForm):
    pet_name = StringField('Pet Name')
    species = StringField('Species')
    photo_url = StringField('Photo URL')
    age = SelectField('Age', choices=[
        ('BBY', 'Baby'),
        ('YNG', 'Young'),
        ('ADT', 'Adult'),
        ('SNR', 'Senior')])
    notes = StringField('Notes')
