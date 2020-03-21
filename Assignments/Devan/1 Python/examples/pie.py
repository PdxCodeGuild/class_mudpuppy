import random

pie_types = ['Marionberry pie', 'Rhubarb pie']
ingredients = ['Marionberry', 'Rhubarb']
in_season = random.choice(ingredients)
print(f"{in_season} are in season!")
chosen_pie = input(f"What kind of pie, {pie_types[0]} or {pie_types[1]}? ")
if chosen_pie == pie_types[0]:  # user chooses berry
    if in_season == ingredients[0]:  # berry in season
        print('Great time for Marionberry pie!')
    elif in_season == ingredients[1]:  # could be an else
        print('Sorry, you missed berry season.')
elif chosen_pie == pie_types[1]:  # user chooses rhubarb
    if in_season == ingredients[0]:  # berry in season
        print('You missed rhubarb season!')
    else:
        print('We do have Rhubarb!')
