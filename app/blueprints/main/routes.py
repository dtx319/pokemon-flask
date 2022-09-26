from . import bp as app
from flask import render_template, request, redirect, url_for, flash
from app.blueprints.main.models import User, Pokemon, Post
from app import db
from flask_login import current_user, login_required

# Routes that return/display HTML


@app.route('/')
@login_required
def home():
    pokemon = Pokemon.query.all()

    return render_template('home.html', user=current_user, pokemon=pokemon)

@app.route('/about')
@login_required
def about():
    return render_template('about.html')

@app.route('/contact')
@login_required
def contact():
    return render_template('contact.html')

@app.route('/capture_pokemon', methods=['POST'])
@login_required
def capture_pokemon():
    pokemon_name = request.form['name']
    pokemon_description = request.form['description']
    pokemon_type = request.form['type']
    
    new_pokemon = Pokemon(name=pokemon_name, description=pokemon_description, type=pokemon_type, user_id=current_user.id)

    db.session.add(new_pokemon)
    db.session.commit()

    flash('Pokemon added successfully', 'success')
    return redirect(url_for('main.home'))

