# import random
# computer = random.randint(1,10)
# def user_guess():
#     while True:
#         for i in range (10):
#             user_guess = int(input(f"What is the computer guess? "))
#         user_guess = 9-i
#     if user_guess == computer:
#         print("Correct! ")
#     else:
#         print("Try again! ")
    
"""
Version 2
"""

import random 
computer = random.randint(1,10)
print(computer)

counter1 = 0
while True:
    counter1 = int(counter1 + 1)
    user_guess = (input(f"what is the computer guess? "))
    if user_guess == 'stop':
        break
print(f"You guessed {counter1} times. ")

"""
version 3
"""
import random 
computer = random.randint(1,10)
print(computer)

counter1 = 0
while True:
    counter1 = int(counter1 + 1)
    user_guess = (input(f"what is the computer guess? "))
if user_guess > computer:
    print("Too high! ")
elif user_guess < computer:
    print("Too low! ")









