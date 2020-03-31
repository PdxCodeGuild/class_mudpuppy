# turn_right.py
import random
directions = ['North', 'East', 'South', 'West']
start_direction = random.randint(0, 3)
print(f"You are facing {directions[start_direction]}.")
turn_right = int(input("Turn right how many times? "))
direction = start_direction + turn_right
print(f"You are facing {directions[direction % len(directions)]}.")