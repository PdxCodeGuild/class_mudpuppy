#Lab 12, version 3, March 26th, 2020
import random

num1 = random.randint(1,10)

guess_tally = 0

def too_high(x, y):
    return x > y

def too_low(x, y):
    return x < y

while True:
    user_guess = int(input("What number do you guess? : "))

    if user_guess == num1:
        guess_tally = guess_tally + 1
        print(f"You're correct! You guessed {guess_tally} time(s).")
        break

    if user_guess != num1:
        guess_tally = guess_tally + 1

        if too_high(user_guess, num1) == True:
            print("Your guess is too high, try again.")
        
        if too_low(user_guess, num1) == True:
            print("Your guess is too low, try again.")
