#Lab 12, version 2, March 26th, 2020

import random

num1 = random.randint(1,10)

guess_num = 0

while True:
    user_guess = int(input("What number do you guess? : "))

    if user_guess == num1:
        guess_num = guess_num + 1
        print(f"You're correct! You guessed {guess_num} time(s).")
        break

    if user_guess != num1:
        guess_num = guess_num + 1
        print("Guess again!")
    
