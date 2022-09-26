from . import bp as app
from flask import render_template

trainer_data = { 
    'dennisx': {
        'user_id': 0,
        'name': 'Dennis',
        'pokemon': [
            {
                'id': 0,
                'name': 'Jigglypuff',
                'description': 'The best pop singer in the pokemon world!',
                'type': 'Fairy',
                'user_id': 1
            },
            {
                'id': 0,
                'name': 'Gengar',
                'description': 'Boo!',
                'type': 'Ghost-Poison',
                'user_id': 1
            },
        ]
    }
}

# Create a route to get all user information
@app.route('/trainers/')
def trainers():
    return trainer_data

# Create a route to get user information based on their username
@app.route('/trainer/username/<username>')
def trainer(username):
    if username not in trainer_data:
        return 'Trainer not found'

    return trainer_data[username]

# Create a route to get user information based on their id
@app.route('/user/id/<id>')
def user_by_id(id):
    for key, trainer in trainer_data.items():
        if trainer['trainer_id'] == int(id):
            return trainer

    return 'Trainer not found'


pokemon_data = [
        {
            'id': 3,
            'name': 'Alakazam',
            'description': 'The Great Houdini in Pokemon form.',
            'type': 'Psychic',
            'user_id': 1
        },
            {
                'id': 4,
                'name': 'Mew',
                'description': 'The original pokemon.',
                'type': 'Psychic',
                'user_id': 1
            },
]


@app.route('/pokemon/')
def pokemon():
    return pokemon_data

@app.route('/pokemon/id/<id>')
def pokemon_by_id(id):
    if int(id) not in pokemon_data:
        return 'Pokemon not found'

    return pokemon_data[int(id)]