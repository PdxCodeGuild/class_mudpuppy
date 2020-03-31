# import random

# eye = random.choice(';:')
# nose = random.choice('->')
# mouth = random.choice(')]')
# output = eye + nose + mouth
# print(output)

# def make_face(eye, nose, mouth):
#     return eye + nose + mouth

# # def make_eye():
# #     return 

# # def make_nose():
# #     return 

# # def make_mouth():
# #     return 

# #print(make_face(make_eye(), make_nose(), make_mouth()))
# #print(make_face(';', '>', ']'))


#TRYING TO GET THE COMPUTER TO MAKE AN OPTIMAL GUESS THROUGH AVERAGES AND FEEDBACK
def average(x, y):
    return round((x + y) / 2)

def search(lower, upper, target, guess):
    print(f'You guessed {guess}')

    if guess == target:
        print('Correct!')

    elif guess < target:
        print('Too low!')
        search(guess, upper, target, average(guess, upper))
    elif guess > target:
        print('Too high!')
        search(lower, guess, target, average(lower, guess))

search(1, 100, 1, 2)

