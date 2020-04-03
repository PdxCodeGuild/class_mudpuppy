# favorite_colors.py
favorite_colors = ['blue', 'purple', 'red']
color_guesses = []
for _ in favorite_colors:
    one_guess = input("Guess one of my favorite colors: ")
    color_guesses.append(one_guess.lower())
color_guesses.sort()
favorite_colors.sort()
if color_guesses == favorite_colors:
    print("Correct")
else:
    print("Incorrect")