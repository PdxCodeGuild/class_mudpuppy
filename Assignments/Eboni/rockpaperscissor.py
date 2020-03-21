"""
Let's play rock-paper-scissors with the computer.

The computer will ask the user for their choice (rock, paper, scissors)
The computer will randomly choose rock, paper or scissors
Determine who won and tell the user
"""
import random

move_types = ['rock', 'paper', 'scissors ']
# move_types = int('move_types')
user = input(f"Choose rock, paper, or scissors ")
#user = False
computer = random.choice(move_types)
print(f"You chose {user}" )
print(f"Computer chose {computer}" )
if user == computer:
    print("Tie!")

if user == move_types[0]:
    if computer == move_types[1]:
        print("Computer wins!")
    elif computer == move_types[2]:
        print("User wins!")

if user == move_types[1]:
    if computer == move_types[2]:
        print("Computer wins!")
    elif computer == move_types[0]:
        print("User wins!")

if user == move_types[2]:
    if computer == move_types[0]:
        print("Computer wins!")
    elif computer == move_types[1]:
        print("User wins!")

again = input("Would you like to play again? ")
    
    





   
    





