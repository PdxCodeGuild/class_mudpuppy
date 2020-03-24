# what movie.py

movie_dict = {'Eboni': 'The Shining', 'Devan': 'Borat', 'Brea': '500 Days of Summer', 'Terrance': 'Black Hawk Down',
              'Manny': 'Inglorious Basterds', 'Kadir': 'Black Panther', 'Al': 'Knives Out', 'Evan': 'The Producers'}

user_name = input("What's your name? ").lower()

if movie_dict.keys():  # their name is in the dictionary:
    print(f'You want to watch {movie_dict[user_name]}')
else:
    print('I don\'t know what you want to watch.')
