"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    name = StringField(
        'Pet Name',
        validators=[InputRequired()])

    species = SelectField(
        'Species',
        choices=[
            ('CAT', 'Cat'),
            ('DOG', 'Dog'),
            ('PORC', 'Porcupine')],
        validators=[InputRequired()])

    photo_url = StringField(
        'Photo URL',
        validators=[Optional(), URL()])

    age = SelectField(
        'Age',
        choices=[
            ('BBY', 'Baby'),
            ('YNG', 'Young'),
            ('ADT', 'Adult'),
            ('SNR', 'Senior')],
        validators=[InputRequired()])

    notes = StringField('Notes')


class EditPetForm(FlaskForm):
    photo_url = StringField(
        'Photo URL',
        validators=[Optional(), URL()])

    notes = StringField('Notes')

    available = BooleanField("Is available", default="checked")
