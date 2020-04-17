import random
# '''options = [rock, paper, scissor]
# tie = [rock vs rock]'''
print("WELCOME TO ROCK-PAPER-SCISSORS")
options = ["rock", "paper", "scissors"]
# print("WELCOME TO ROCK-PAPER-SCISSORS")
user = input(f'choose one: {options}').lower()
# computer = "rock", "paper", "scissors"
computer = (random.choice(options))
# options = ["rock", "paper", "scissor"]
# # tie = [rock vs rock]
# print(random.choice(options))

# rock1 = rock is > scissors
# scissor is > paper
# paper is > rock
tie = (f"computer chose {computer} & you chose {user} issa tie")
uwin = (f"You won!!\ncomputer chose {computer} & you chose {user}")
iwin = (f"I won!!\n computer chose {computer} & you chose {user}")

# r = "rock"
# p = "paper"
# s = "scissors"

# def function(user,computer):
if user == computer:
    print(tie) #return "issa tie" #print(tie)
elif user == "rock" and computer == "paper":
    print(iwin) #return "I Win" #print(iwin)
elif user == "rock" and computer == "scissors":
    print(uwin) #return "You win" #print(uwin)
elif user == "paper" and computer == "rock":
    print(uwin) #return "You win" #print(uwin)
elif user == "paper" and computer == "scissors":
    print(iwin) #return "I win" #print(iwin)
elif user == "scissors" and computer == "rock":
    print(iwin) #return "I win" #print(iwin)
elif user == "scissors" and computer == "paper":
    print(uwin) #return "I win" #print(uwin)

# else:
#     print("try again")
# print(function(user,computer))