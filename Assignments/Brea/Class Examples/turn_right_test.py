#Turn_right.py
import random

directions = ['North', 'East', 'South', 'West']
start_direction = random.randint(0, 3)
print(f"You are facing {directions[start_direction]}")

turn_right = int(input("Turn right how many times? : "))

direction = start_direction + turn_right
print(f"You are facing {directions[direction % len(directions)]}.") #uses modulus to minus 4 (the length of the list) at every chance, to loop back to beginning of the list


#counter = count + 1 is same as counter += 1

#rotate.py
from time import sleep
directions = ['up', 'right', 'down', 'left']
facing = 0
while True:
    print(directions[facing % 4]) #or, % len[directions]
    facing += 1 #facing = facing + 1
    sleep(.2) #slows down how fast the computer runs the code