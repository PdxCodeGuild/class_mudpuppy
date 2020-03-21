import random

choices = ['Rock', 'Paper', 'Scissors']
computer = choices[random.randint(0,2)]
print('Let\'s play Rock, Paper, Scissors!')
player = input('Rock, Paper, Scissors? ')
if player == computer:
    print('Tie!')
elif player == 'Rock':
    if computer == 'Paper':
        print(f'You lose {computer} covers {player}')
    else:
        print(f'You win! {player} smashes {computer}')
elif player == 'Paper':
    if computer == 'Scissors':
        print(f'You lose, {computer} cut {player}')
    else:
        print(f'You win! {player} covers {computer}')
elif player == 'Scissors':
    if computer == 'Rock':
        print(f'You lose, {computer} smashes {player}')
    else:
        print(f'You win! {player} cuts {computer}')
else:
    print('Please check your spelling!')
