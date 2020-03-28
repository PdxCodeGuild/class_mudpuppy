#Lab 12, version 4, March 26th, 2020

import random

num1 = random.randint(1,10)

guess_tally = 0

first_run = True
while True:
    user_guess = int(input("What number do you guess? : "))

    if user_guess == num1:
        guess_tally = guess_tally + 1
        print(f"You're correct! You guessed {guess_tally} time(s).")
        break
    
    if first_run == True:
        old_guess = user_guess
        first_run = False

    if user_guess != num1:
        guess_tally = guess_tally + 1

        if user_guess > num1:
            feedback1 = abs(old_guess - num1)

            if 
        
        if abs(user_guess) < old_guess and user_:
            feedback_low abs(old_guess - num1)
            print("You're getting closer!")
        
