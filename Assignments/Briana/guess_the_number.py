# import random
# while True:


#     computer = random.randint(1,3)
#     print('Guess a number ')
#     user_input = input()
#     print('the users input is: ')
#     print(user_input)
#     if int(user_input) == computer :
#     #if bla==2 :
#         print(computer)
#         print('You Win!')
#         # break
#     elif user_input != computer : 
#         print('the comps input is: ')
#         print(computer)
#         print('Try again')

#     if int(user_input) > computer:
#         print("Too high!")
#     elif int(user_input) < computer:
#         print("Too low!")


# Version 2 and 4

import random

guess_counter = 0


while True:

    computer = random.randint(1,3)

    print('Guess a number or enter \'done\' \n')
    user_input = input()
    print('the users input is: ')
    print(user_input)
    if(user_input) == 'done':
        print('You guessed ')
        print(guess_counter)
        print('times.')
        break
    if int(user_input) == computer :
        guess_counter +=1
    #if bla==2 :
        print(computer)
        print('You Win!')
        # break
    elif user_input != computer : 
        guess_counter +=1
        print('the comps input is: ')
        print(computer)
        print('Try again')

    if int(user_input) > computer:
        print("Too high!")
    elif int(user_input) < computer:
        print("Too low!")

    
