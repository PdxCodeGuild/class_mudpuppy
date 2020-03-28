import random

comp_num = random.randint(1, 10)
guess_count = 0
last_guess = None


def find_diff(comp_num, usr_num):
    return abs(comp_num - usr_num)


while True:
    usr_num = int(input('\nGuess a number between 1 and 10: '))
    if usr_num == comp_num:
        print(f'\nCorrect, the number was {comp_num}. You guessed it in {guess_count} guesses.')
        break

    print('\nSorry you\'re wrong.')

    if last_guess is not None:
        a_guess = find_diff(comp_num, usr_num)
        a_last_guess = find_diff(comp_num, last_guess)
        if a_guess < a_last_guess:
            print('You\'re getting warmer.')
        elif a_guess > a_last_guess:
            print('You\'re getting colder.')
        elif a_guess == a_last_guess:
            print('You entered the same number....')

    print('\nYou guessed: ' + str(usr_num))
    print('Your last guess was: ' + str(last_guess))

    last_guess = usr_num
    guess_count += 1
