import random
print("Welcome to Rock, Paper, Scissors")


choices = ["rock", "paper", "scissors"]
user = input(f"Choose one: {choices} \n").lower() #\n gives us a new line, /t = tab

win = "You win!"
lose = "You lose!!!"
tie = "You tied"

computer = (random.choice(choices))

if user == computer: #if user == "rock" and computer == "rock":
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
