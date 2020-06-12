[//]: # (
    TODO:
    * Make a separate pipenv file
    * Link to that
    * Advise pipenv use, for windows compatability
)

# Contacts Lab with Fake Django

## Introduction

The goal of this tutorial is to make a fake version of Django, and to complete part of the contacts lab with it. Ideally we should be able to generate webpages from an html template. We will parse the url path for a name, search our CSV file for the name, and use that contact's information to populate our html template and then provide a response.

## Part 1
### Starting with Flask

Flask is a lot like Django, but smaller. To start, we are going start a [pipenv environment](pipenv.md). Make a new folder called `flask_contacts`, `cd` into it in terminal or Powershell, and then run:

```
py -m pipenv install
py -m pipenv install flask
py -m pipenv shell
```

Then we will follow the instructions on the Flask quickstart, [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/). You might have to replace this command:
```
flask run
```

with this command:
```
py -m flask run
```

## Part 2
### Experimenting with Flask

Change the file to look like this (except don't copy where it says `New line`, `Changed line`, or `Removed line`). The coloring is a bit weird in this one because it doesn't see `New line` as a comment when it's between two sets of `'''`, because `'''` will open or close a large multi-line string.


```python
from flask import Flask
app = Flask(__name__)

@app.route('/contacts/') # Changed line
def hello_world():
    output = ''' # New line
    <h1>Info about Al</h1> # New line
    <ul> # New line
    	<li>Food: Nachos</li> # New line
    	<li>Game: Dark Souls</li> # New line
    </ul> # New line
    ''' # New line
	return output # Changed line
```
Go to the terminal or Powershell where you ran the server. Push `Ctrl C` to kill the server, and then up and enter to run it again.

Now, we should be able to go to the address in our browser, `http:127.0.0.1:5000/`, but it will tell us that it couldn't find anything at that url.

Because we changed a line from `@app.route('/')` to `@app.route('/contacts/')`, we need to put this into our browser's location bar: `http:127.0.0.1:5000/contacts/`. Now we should see all that html in our `output` string rendered in the browser.

Right now this works for one contact. If we want it to work for multiple potential contacts, we'll have to let it accept variables.

```python
from flask import Flask
import random # New line
app = Flask(__name__)

@app.route('/contacts/')
def hello_world():
    output = '''
    <h1>Info about name_var</h1> # Changed line
    <ul>
        <li>Food: food_var</li> # Changed line
        <li>Game: game_var</li> # Changed line
    </ul>
    '''

    contacts = ( # New line
        ('Al', 'Nachos', 'Dark Souls'), # New line
        ('Pete', 'Sushi', 'New Vegas'), # New line
        ('Eboni', 'Ramen, 'Assassin's Creed III'), # New line
    ) # New line

    contact = random.choice(contacts) # New line
    output = output.replace('name_var', contact[0]) # New line
    output = output.replace('food_var', contact[1]) # New line
    output = output.replace('game_var', contact[2]) # New line
    return output
```

Go to the terminal or Powershell where you ran the server. Push `Ctrl C` to kill the server, and then up and enter to run it again.

Go to the page and refresh it multiple times. You should see multiple random names come up.

This is going well, but what if you wanted to find contact info on a specific person, then you'd have to spam the refresh button until you randomly got the correct person. It'd be way cooler if someone could put the name in the url and find the contact.

## Part 3
### Setting up Contacts

Our first goal should be to just print out the name that we want to search for.

```python
@app.route('/contacts/<name>/') # Changed line
def by_name(name): # Changed line
    print(name) # New line
	output = '''
```
Go to the terminal or Powershell where you ran the server. Push `Ctrl C` to kill the server, and then up and enter to run it again.

Now you should be able to go to `http:127.0.0.1:5000/contacts/abc/`, and then we can look at the terminal or Powershell, and it should print out `abc`. We're not actually using that `abc` anywhere, but we successfully got it into the function as the variable `name` and printed it out.

Let's offload the contact info into a CSV file. First, we can delete some lines from hello.py:

```python
    # contacts = ( # Removed line
        # ('Al', 'Nachos', 'Dark Souls'), # Removed line
        # ('Pete', 'Sushi', 'New Vegas'), # Removed line
        # ('Eboni', 'Ramen', 'Assassin's Creed III'), # Removed line
    # ) # Removed line

    # contact = random.choice(contacts) # Removed line
```

Also, delete the `import random` line near the top. Now we can make a file called `contacts.csv` that looks like this:

```csv
Al,Nachos,Dark Souls
Pete,Sushi,New Vegas
Eboni,Ramen,Assassin's Creed III
```

And a file called `contacts.py` that looks like this:

```python
print("You are running or importing contacts.py!")

class Contact:
    def __init__(self, name_param, food_param, game_param):
        self.name_attr = name_param
        self.food_attr = food_param
        self.game_attr = game_param

    @staticmethod
    def find_contact(search_name):
        with open('contacts.csv', 'r') as f:
            for line in f.readlines():
                line = line.split(',')
                if search_name.lower() == line[0].lower():
                    return Contact(
                        name_param = line[0],
                        food_param = line[1],
                        game_param = line[2],
                    )

found_contact = Contact.find_contact('Al')
print(found_contact.name_attr, found_contact.food_attr, found_contact.game_attr)
```

Our `Contact` class will hold all the information of a contact. It's similar to a dictionary. Our `find_contact` function gives us an instance of the `Contact` class.

Basically, we can use `find_contact` to search our csv for a name, and then that will create a contact from the blueprint `Contact` that has the attributes `name_attr`, `food_attr`, and `game_attr`.

The last two lines are unnecessary, I just wanted to test out the file. Often people will make lines like this run if you run the file directly, but be ignored if you are importing the file. You can do this by changing the file like this:

```python
if __name__ == "__main__":
    found_contact = Contact.find_contact('Al')
    print(found_contact.name_attr, found_contact.food_attr, found_contact.game_attr)
```

We can use this file in our `hello.py` file. First, we need to import it:

```python
from flask import Flask
from contacts import Contact # New line
```

And then we can use our `Contact` class inside our `hello.py` file by changing `hello.py` like this:

```python
    found_contact = Contact.find_contact(name) # New line
    output = output.replace('name_var', found_contact.name_attr) # Changed line
    output = output.replace('food_var', found_contact.food_attr) # Changed line
    output = output.replace('game_var', found_contact.game_attr) # Changed line
    return output
```

Kill and restart the server, and then fake Django should be up and running!

Now imagine our csv looks like this:

```csv
Al,Nachos,Dark Souls
Pete,Sushi,New Vegas
Eboni,Ramen,Assassin's Creed III
Al,Soup,Tetris
```

We have two people named `Al`, so we're never going to pull out the second one. This system could work better if instead of searching by name we gave the option to search by a unique ID number. First, let's change the CSV:

```csv
1,Al,Nachos,Dark Souls
2,Pete,Sushi,New Vegas
3,Eboni,Ramen,Assassin's Creed III
4,Al,Soup,Tetris
```
Because we added a new column to the CSV we're going to need to increment a bunch of the indecies we use to look up information. We can also add a new function:
```python
                if search_name.lower() == line[1].lower(): # Changed line
                    return Contact(
                        name_param = line[1], # Changed line
                        food_param = line[2], # Changed line
                        game_param = line[3], # Changed line
                    )

    @staticmethod # New line
    def find_by_id(search_id): # New line
        with open('contacts.csv', 'r') as f: # New line
            for line in f.readlines(): # New line
                line = line.split(',') # New line
                if search_id == line[0]: # New line
                    return Contact( # New line
                        name_param = line[1], # New line
                        food_param = line[2], # New line
                        game_param = line[3], # New line
                    ) # New line
```

Since there's some repeated code here, we could potentially restructure the code to be cleaner, but let's not worry about that now.

Now we just need to add a new function into our `hello.py` file:

```python
@app.route('/contacts/id/<contact_id>/')
def by_id(contact_id):
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
```
Again, there's some repeated code, which means that it could be cleaner. This is fine for now, though.

Kill and restart the server, and then try searching by name and by id number.
