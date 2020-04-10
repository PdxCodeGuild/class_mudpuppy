#lab12-guess_the_number.py


import random

counter = 0

computer_num = random.randint(1, 10)
#print (computer_num)

print(f"Let's play 'Guess the Number'. The computer will guess a random int between 1 and 10. The user will then try to guess the number, and the program will tell them whether they're right or wrong.")

running = True
while running:
    user_guess = int(input("What is your guess? "))
    if user_guess == computer_num:
        running = False
        print("Correct")
        print(f"Great job! you got it correct in {counter + 1} times!")
    else: 
        print("Wrong")
        counter = counter + 1
    if user_guess > computer_num:
        print("Your guess was too high!")
    if user_guess < computer_num:
        print("Your guess was too low!")
    
