#what_move.py
movie_dict = {'Eboni': 'The Shining', 'Devan': 'Borat', 'Brea': '500 Days of Summer', 'Terrance': 'Black Hawk Down', 'Manni': 'Inglorious Basterds', 'Kadir': 'Balck Panther', 'Al': 'Knives Out', 'Evan': 'The Producers'}

# go_again = input("Play again? ").lower()
#     if go_again in ['y', 'yes', 'n', 'no']

# input(':').lower()
# print(input)

user_name = input ("What's your name? ")

if user_name in movie_dict.keys(): #their name is in our dictionary:
    print(f"You want to watch {movie_dict[user_name]}") #recommend a move
else:
    print("I don't know what you want to watch.")
