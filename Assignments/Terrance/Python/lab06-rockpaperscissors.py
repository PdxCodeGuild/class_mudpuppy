lab07-rockpaperscissors.py

import random
user_input = 'yes'

while user_input == 'yes':

    print('Let\'s play rock-paper-scissors!')
    print('The computer will ask the user for their choice of rock, paper or scissors, and then the computer will randomly make a selection.')
    #computer tell user how the game will work
    user = input ('rock, paper or scissors:')

    choices = ('rock', 'paper', 'scissors')
    #the user will have to choose one of these options
    computer = random.choice(choices)
    #the computer will select a random choice
    if user == computer:
        print('It\'s a tie')
    elif user == 'rock':
        if computer == 'paper':
            print('Computer wins, the computer chose paper')
        if computer =='scissors':
            print('Computer loses, the computer chose scissors' )
    elif user == 'paper':
        if computer =='scissors':
            print('Computer wins, the computer chose scissors' )
        if computer == 'rock':
            print('Computer loses, the computer chose rock')
    elif user == 'rock':
        if computer =='scissors':
            print('Computer loses, the computer chose scissors' )
        if computer == 'rock':
            print('Computer wins, the computer chose rock')

    user = input('Would you like to play again?')

    








