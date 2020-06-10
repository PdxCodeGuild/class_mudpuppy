from flask import Flask
app = Flask(__name__)

@app.route('/contacts/') # Changed line
def hello_world():
    output = 
    <h1>Info about Al</h1> # New line
    <ul> # New line
    	<li>Food: Nachos</li> # New line
    	<li>Game: Dark Souls</li> # New line
    </ul> # New line
    
	return output # Changed line