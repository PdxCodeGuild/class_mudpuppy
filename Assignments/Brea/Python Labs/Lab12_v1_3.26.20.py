#Lab 12 Version 1, March 26th, 2020

import random

num1 = random.randint(1,10)

guess_num = 0

while True:
    user_guess = int(input("What number do you guess? : "))

    if user_guess == num1:
        guess_num = guess_num + 1
        print(f"You're correct! You guessed {guess_num} of times.")
        break

    if user_guess != num1:
        guess_num = guess_num + 1
        print("Guess again!")

    if guess_num == 10:
        print("Sorry, game over!")
        break