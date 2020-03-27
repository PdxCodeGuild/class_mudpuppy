import random

comp_num = random.randint(1, 10)

for i in range(10):
    usr_num = int(input('Guess a number between 1 and 10: '))
    if usr_num == comp_num:
        print(f'Correct, the number was {comp_num}. ')
        break

    print(f'Wrong, you have {9 - i} guesses remaining.')
