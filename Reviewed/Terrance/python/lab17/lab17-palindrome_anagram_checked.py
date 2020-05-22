#lab17-palindrome_and_anagram.py

first_word = input("Enter your first word: ")
print (f"The first word you entered is: {first_word}")
first_word = first_word.lower()

second_word = input("Enter your second word: ")
print (f"The second word you entered is: {second_word}")
second_word = second_word.lower()

first_word = list(first_word)
print(first_word) # nice prints, lets you see every step

second_word = list(second_word)
print(second_word)
'''
Consider experimenting with combining some of these lines

first_word = list(input("First word: ").lower())
second_word = list(input("Second word: ").lower())
'''

first_word.sort()
print(first_word)

second_word.sort()
print(second_word)

if first_word == second_word:
    print("True")



def palindrome(user_input):
    user_input_reverse = user_input[::-1]
    return user_input == user_input_reverse
# Let me know if you want to do this lab the other way

user_input = input("Enter a word: ")

print (palindrome(user_input)) # Cool function!
