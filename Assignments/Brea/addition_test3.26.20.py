#addition_test.py
import random

num1 = random.randint(1,5)
num2 = random.randint(1,5)
running = True

while running:
    user_guess = int(input(f"What is {num1} + {num2}? : "))

    if user_guess == num1 + num2:
        running = False
        print("Correct!")
    
    else:
        print("Wrong!")