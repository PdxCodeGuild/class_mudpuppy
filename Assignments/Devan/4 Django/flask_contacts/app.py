from flask import Flask
import random
app = Flask(__name__)


@app.route('/contacts/')
def hello_world():
    output = '''
    <h1>Info about name_var</h1>
    <ul>
        <li>Food: food_var</li>
        <li>Game: game_var</li>
    </ul>
    '''

    contacts = (
        ('Al', 'Nachos', 'Dark Souls'),
        ('Pete', 'Sushi', 'New Vegas'),
        ('Matthew', 'Veggie Burger', 'Halo'),
        ('Devan', 'Street Tacos', 'No Mans\'s Sky'),
    )

    contact = random.choice(contacts)
    output = output.replace('name_var', contact[0])
    output = output.replace('food_var', contact[1])
    output = output.replace('game_var', contact[2])
    return output
