from random import randint

directions = ['North', 'East', 'South', 'West']
start_directon = randint(0, 3)
print(f'You are facing {directions[start_directon]}')
turn_right = int(input('Turn right how many times? '))
direction = start_directon + turn_right
print(f'You are facing {directions[direction % len(directions)]}')
