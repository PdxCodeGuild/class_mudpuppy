# import random
from flask import Flask
from contact import Contact
# from flask import Flask
app = Flask(__name__)
# '''
# @app.route('/contacts/')


# def hello_world():
#     output="""<h1>Info about name_var</h1>
#     <ul>
#         <li> Food: food_var</li>
#         <li>Game: game_var</li>
#     </ul>
#     """
    
#     contacts = (
#         ('Al', 'Nachos', 'Dark Souls'),
#         ('Pete', 'Sushi', 'New Vegas'), 
#         ('Matthew', 'Veggie Burger', 'Halo'), 
#     ) 
    
#     contact = random.choice(contacts) 

#     output = output.replace('name_var', contact[0])
#     output = output.replace('food_var', contact[1]) 
#     output = output.replace('game_var', contact[2]) 
    
#     return output
# '''

@app.route('/contacts/<name>/')

def by_name(name):
    print(name)
    output="""
    <h1>Info about name_var</h1>
    <ul>
        <li> Food: food_var</li>
        <li>Game: game_var</li>
    </ul>
    """
    # if __name__ == "__main__":
    found_contact = Contact.find_contact(name) 
   
    # print(found_contact.name_param, found_contact.food_param, found_contact.game_param)
    output = output.replace('name_var', found_contact.name_attr)
    output = output.replace('food_var', found_contact.food_attr) 
    output = output.replace('game_var', found_contact.game_attr) 

    return output 