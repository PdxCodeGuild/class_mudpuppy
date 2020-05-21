#Lab 12, version 5 March 26th, 2020
import random

user_guess = int(input("What number do you choose? : "))

guess_tally = 0

while True:
    num1 = random.randint(1,10)
    print(f"I choose {num1}")

    if num1 == user_guess:
        guess_tally = guess_tally + 1
        print(f"I guessed the right number in {guess_tally} time(s).")
        break

    if num1 != user_guess:
        guess_tally = guess_tally + 1
        print("Drats, I'll try again.")
