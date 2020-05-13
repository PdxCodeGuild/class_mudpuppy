import random
user_input = input("Give me a movie: ")
opinions = ['good', 'bad']
print(
        f"You chose the movie { user_input } and that is a { random.choice(opinions) } choice."
)
