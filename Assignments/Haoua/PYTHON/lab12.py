import random

# choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# user = int(input(f"pick a number between 1-10 : "))
# num = int(random.randint(0,10)) #random integer between 1 and 10
# print(num)

# # user = ''
# guess_count = 0
# guess_limit = 10
# out_of_guesses = False

# # while guess <= guess_limit:
# #     if num != user:
# #         user = int(input("Guess again : ")
# #         guess = guess + 1 
# #     elif num == user:
# #         guess = guess + 1
# #         print("correct")
# #     elif num > user:
# #         guess = guess + 1
# #         print("too low")
# #     elif num < user:
# #         guess = guess + 1
# #         print("too high")_
# while num != user and not out_of_guesses:
#     # user = int(input("Guess again : "))
#     if guess_count < guess_limit:
#         user = int(input("Guess again : "))
#         num = print(random.randint(0,10))
#         guess_count += 1
#     elif num == user:
#         print("correct")
#         guess += 1
#         break
#     elif num > user:
#         print("too low!")
#         guess += 1
#         break
#     elif num < user:
#         print("too high!")
#         guess += 1
#         break
#     # print("guesses:   ", guess)
#     else:
#         out_of_guesses = True

# if out_of_guesses:
#     print("out of guesses, you lose!")
# else:
#     print("You win")

'''
        break
    elif num == user:
        print("correct")
        guess += 1
        break
    elif num > user:
        print("too low!")
        guess += 1
        break
    elif num < user:
        print("too high!")
        guess += 1
        break
    # print("guesses:   ", guess)
'''

'''Building a guessing game''' #input secret word, if they do not guess it continue to ask.
secret_word = random.randint(0,10) #created variables
guess =int(input("Enter Guess : "))
print(secret_word)
guess_count = 0 #everytime the loop goes around add 1 for the guess
guess_limit = 10 #how many tries the user has
out_of_guesses = False #will tell us whether or not the user is out of guesses


# if guess_limit < 10:
#     out_of_guesses = False
# # else:
# #     out_of_guesses = True

while guess != secret_word and not(out_of_guesses): #as long as they haven't guessed the word or are out of guesses 
    if (guess_count) < guess_limit: #if guess count is less than guess limit than they have guesses left.
        guess = int(input("Enter guess again: ")) #if they have guesses look we ask them to enter another guess
        # secret_word = print(random.randint(0,10))
        guess_count += 1
        print(guess_count)
        
    if secret_word == guess:
        guess_count += 1 
        print("correct")
        
        print(guess_count)
    if secret_word > guess:
        guess_count += 1
        print("too low")
        print(guess_count)
        
    if secret_word < guess:
        guess_count += 1
        print("too high")
        print(guess_count)
        break
    else:
        out_of_guesses = True #if it is equal to true then they don't get anymore guesses
        print("Out of guesses, you lose")
        
print(guess_count)
# if secret_word in guess:
#     guess = guess + 1
#     print("correct")
# elif secret_word > guess:
#     guess = guess + 1
#     print("too low")
# elif secret_word < guess:
#     guess = guess + 1
#     print("too high")
# else:
#     print("Try again")


# if out_of_guesses:
#     print("out of guesses, you lose!")

# else:
#     print("You win")