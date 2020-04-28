import random
while True:
    print('Lets play rock, paper, scissors!')
   
    print('Which do you choose?')
    user = input()

#  name_input = input( " Whats your name. " )

    choices = ["rock" , "paper" , "scissors"]
    computer = random.choice(choices)
    # if user == "rock" and computer == "rock"
    #     print("Tie!")
    #
    #     OR
    if user == computer:
        # print(f"Computer also chose {user} ! ")
        print("Tie!")
        print("Great minds think alike")
    elif user == "rock" and computer == "paper":
        print("Computer's choice: Paper")
        print("You lose!")
    elif user == "rock" and computer == "scissors":
        print("Computer's choice: Scissors")
        print("You Win!")
    elif user == "paper" and computer == "rock":
        print("Computer's choice: Rock")
        print("You win!")
    elif user == "paper" and computer == "scissors":
        print("Computer's choice: Scissors")
        print("You win!")
    elif user == "scissors" and computer == "rock":
        print("Computer's choice: Rock")
        print("You Lose!")
    elif user == "scissors" and computer == "paper":
        print("Computer's choice: Paper")
        print("You win!")

    run_again = input("Would you like to complete another Madlib? ")
    
    while run_again != "no" and run_again != "yes":
        run_again = input("Would you like to complete another Madlib? ")
    if run_again == 'no':
        break