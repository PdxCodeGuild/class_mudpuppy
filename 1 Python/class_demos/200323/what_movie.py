# what_movie.py

movie_dict = {'Eboni': 'The Shining', 'Devan': 'Borat', 'Brea': '500 Days of Summer', 'Terrance': 'Black Hawk Down', 'Manny': 'Inglorious Basterds', 'Kadir': 'Black Panther', 'Al': 'Knives Out', 'Evan': 'The Producers'}

user_name = input("What's your name? ")

if user_name in movie_dict.keys(): # their name is in our dictionary:
    print(f"You want to watch {movie_dict[user_name]}")
else:
    print("I don't know what you want to watch.")