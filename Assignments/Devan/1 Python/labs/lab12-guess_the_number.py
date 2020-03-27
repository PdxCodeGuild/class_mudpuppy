import random

comp_num = random.randint(1, 10)

guess_count = 0

while True:
    usr_num = int(input('Guess a number between 1 and 10: '))
    if usr_num == comp_num:
        print(f'\nCorrect, the number was {comp_num}. You guessed it in {guess_count} guesses.')
        break
    elif usr_num > comp_num:
        guess_count += 1
        print(f'\nToo high. ')
    elif usr_num < comp_num:
        guess_count += 1
        print(f'\nToo low. ')
