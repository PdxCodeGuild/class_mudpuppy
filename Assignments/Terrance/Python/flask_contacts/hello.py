

from flask import Flask
from contacts import Contact
app = Flask(__name__)

@app.route('/contacts/<contact_id>/')
def by_name(contact_id):
    print(contact_id)
    
    output = ''' 

    <ul>
        <li>Food: food_var</li>
        <li>Game: game_var</li>
    </ul>
    '''
  
    found_contact = Contact.find_by_id(contact_id)
    output = output.replace('name_var', found_contact.name_attr)
    output = output.replace('food_var', found_contact.food_attr)
    output = output.replace('game_var', found_contact.game_attr)
    return output
