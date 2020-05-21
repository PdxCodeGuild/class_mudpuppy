#Test Examples, April 29th, 2020

import string

coefficients = [2, 5, 10, 20, 40, 80, 100]

# while user_input not in string.digits: #while the answer is not in the string of good answers
#     print("Not a valid number")

#user_input = input("Type a number between zero and nine : ")



while True:
    user_input = input("Type a number between zero and nine : ")
    user_input = int(user_input)

    try:
        user_input = int(user_input)
        print(f"That number times 10 is {user_input * 10}")
    except ValueError:
        print("not a valid input")



