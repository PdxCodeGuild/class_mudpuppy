import random
import string

choices = ['rock', 'paper', 'scissors']
computerChoice = choices[random.randint(0, 2)]
print('\nLet\'s play Rock, Paper, Scissors!')
playCount = int(input('\nHow many times do you want to play? '))
# for i in range(playCount):
while playCount > 0:
    playerChoice = input('\nRock, Paper, Scissors? ').lower()
    print(f'\nThe computer chose {computerChoice}')
    if playerChoice == computerChoice:
        print('It\'s a Tie!')
    elif playerChoice == 'rock':
        if computerChoice == 'paper':
            print(f'You lose {computerChoice} covers {playerChoice}')
        else:
            print(f'You win! {playerChoice} smashes {computerChoice}')
    elif playerChoice == 'paper':
        if computerChoice == 'scissors':
            print(f'You lose, {computerChoice} cut {playerChoice}')
        else:
            print(f'You win! {playerChoice} covers {computerChoice}')
    elif playerChoice == 'scissors':
        if computerChoice == 'rock':
            print(f'You lose, {computerChoice} smashes {playerChoice}')
        else:
            print(f'You win! {playerChoice} cuts {computerChoice}')
    else:
        print('Please check your spelling!')
    playCount = playCount - 1
    computerChoice = choices[random.randint(0, 2)]
print('\nThanks for playing!')
