"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, Pet

from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def show_pet_listings():
    """
    displays all pets
    (name, photo(if present), and indicates if they are available)

    """

    return render_template('homepage.html')


@app.get('/add')
def display_add_pet_form():
    """renders the add pet form template"""

    return render_template('add_pet_form.html')


@app.route('/add', methods=['GET', 'POST'])
def handle_add_pet_form():
    """add pet form; handle adding"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name,
                      species=species,
                      photo_url=photo_url,
                      age=age,
                      notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {new_pet.name}!")

        return redirect('/')

    else:
        return render_template('add_pet_form.html', form = form)



@app.get('/<pet-id-number>')
def display_pet_info(pet_id_number):
    # <3





@app.post('/<pet-id-number>')
def handle_edit_form(pet_id_number):
    """displays pet information and edit form"""

    pet = Pet.query.get_or_404(pet_id_number)

    form = EditPetForm()

    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

        pet.photo_url = photo_url
        pet.notes = notes
        pet.available = available

        db.session.commit()
        flash(f"Edited {pet.name}!")

        return redirect('/<pet-id-number>')




