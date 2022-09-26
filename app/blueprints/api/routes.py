from . import bp as app
from flask import render_template

trainer_data = { 
    'dennisx': {
        'user_id': 0,
        'name': 'Dennis',
        'pokemon': [
            {
                'id': 0,
                'title': 'This is post 1',
                'body': 'This is the text for the post'
            },
            {
                'id': 1,
                'title': 'This is post 2',
                'body': 'This is the text for the post'
            },
            {
                'id': 2,
                'title': 'This is post 3',
                'body': 'This is the text for the post'
            }
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


# car_data = {
#     0: {
#         "name": "Maruti Swift Dzire VDI",
#         "year": 2014,
#         "selling_price": 450000
#     },
#     1: {
#         "name": "Skoda Rapid 1.5 TDI Ambition",
#         "year": 2014,
#         "selling_price": 370000
#     },
#     2: {
#         "name": "Honda City 2017-2020 EXi",
#         "year": 2006,
#         "selling_price": 158000
#     }
# }

# # Create a route that lists all of the cars in car_data
# @app.route('/cars/')
# def cars():
#     return car_data

# @app.route('/cars/year/<year>')
# def car_by_year(year):
#     car_result = {}

#     for key, car in car_data.items():
#         if car['year'] == int(year):
#             car_result[key] = car

#     return car_result

# @app.route('/cars/id/<id>')
# def car_by_id(id):
#     if int(id) not in car_data:
#         return 'Car not found'

#     return car_data[int(id)]