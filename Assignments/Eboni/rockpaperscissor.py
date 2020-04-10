"""
Let's play rock-paper-scissors with the computer.

The computer will ask the user for their choice (rock, paper, scissors)
The computer will randomly choose rock, paper or scissors
Determine who won and tell the user
"""
import random
# while True:
    # move_types = ['rock', 'paper', 'scissors ']
# move_types = int('move_types')
    # user = input(f"Choose rock, paper, or scissors ")
#user = False
    # computer = random.choice(move_types)
    # print(f"You chose {user}" )
    # print(f"Computer chose {computer}" )
    # if user == computer:
    #     print("Tie!")

    # if user == move_types[0]:
    #     if computer == move_types[1]:
    #         print("Computer wins!")
    # elif computer == move_types[2]:
    #     print("User wins!")

    # if user == move_types[1]:
    #     if computer == move_types[2]:
    #         print("Computer wins!")
    # elif computer == move_types[0]:
    #     print("User wins!")

    # if user == move_types[2]:
    #     if computer == move_types[0]:
    #         print("Computer wins!")
    # elif computer == move_types[1]:
    #     print("User wins!")

    # user_input = input("Would you like to play again? ")
    # if user_input == 'no':
    #     break



choice = {'rock' : ['paper', 'scissor'], 'paper' : ['scissor', 'rock'], 'scissor' : ['rock', 'paper'] }
def choose(player, computer):
    if player == choice[computer][0]:
        print("Player wins! ")
    if player == choice[computer][1]:
        print ("Computer wins! ")
    if player == computer
        print ("Tie! ")

user = input(f"Choose rock, paper, or scissor ")
move_types = ['rock', 'paper', 'scissor']
computer = random.choice(move_types)
choose(user, computer)


    







   
    





