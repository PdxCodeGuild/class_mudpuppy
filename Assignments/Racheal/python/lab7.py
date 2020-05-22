import random

print("Welcome to Rock, Paper, Scissors!!!")

choices = ["rock", "paper", "scissors"]

user = input(f"choose one: {choices}\n")

win = "you win!"
lose = "you lose!"
tie = "you tied!"

# computer = ramdp,.choice(choices)

computer = "rock", "paper","scissors"

computer = random.choice(choices)

if user == computer:
    print(tie)
elif user == "rock" and computer == "scissors":
    print(win)
elif user == "rock" and computer == "paper":
    print(lose)
elif user == "paper" and computer == "rock":
    print(win)
elif user == "paper" and computer == "scissors":
    print(lose)
elif user == "scissors" and computer == "rock":
    print (lose)
elif user == "scissors" and computer == "paper":
    print(win)

print(f'user chose {user} and computer chose {computer}')