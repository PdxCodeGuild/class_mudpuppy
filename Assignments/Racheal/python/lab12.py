import random
num = random.randint(0,10)
print("Guess the Number")

choices = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
user = int(input(f"choose one: {choices}\n"))

# print(num)

correct = "Awesome!"
incorrect = "Please try again"

# computer = "8"

# computer = random.choice(choices)

# print(computer)


# if user == computer:
#     print(correct)
# else:
#     print(incorrect)

# elif user == "1" and computer == "8":
#     print(no)
# elif user == "2" and computer == "8":
#     print(no)
# elif user == "3" and computer == "8":
#     print(no)
# elif user == "4" and computer == "8":
#     print(no)
# elif user == "5" and computer == "8":
#     print (no)
# elif user == "6" and computer == "8":
#     print(no)
# elif user == "7" and computer == "8":
#     print(no)
# elif user == "8" and computer == "8":
#     print(Awesome)
# elif user == "9" and computer == "8":
#     print(no)
# elif user == "10" and computer == "8":
#     print(no)

while num != user:
    user = int((input)("Please try again: "))
    if num == user:
        print("WOO HOO!")
    elif num > user:
        print("too low!")
    elif num < user:
        print("too high!")
        print(num)
        break
# while guess != random.randint:

    #on line 55 
    # while guesses = less than 5 ...add 1 to guesses .. after that you can 
    # print the secret number 


    # randNum 