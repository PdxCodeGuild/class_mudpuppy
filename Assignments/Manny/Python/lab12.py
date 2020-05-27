import random # random 
num1 = random.randint(1,10) # random number that user has to guess 
counter = 0
while True:
    usernum = int(input("Pick a number between 1-10"))
    if usernum == num1:
        counter = counter + 1
        print(f"You're right took you {counter} times")
        break

    if usernum != num1:
        counter = counter + 1
        print("Guess again")