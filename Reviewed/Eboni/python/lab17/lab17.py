# def check_palindrome():
#     user_input = input('word: ')
#     for index in range(len(user_input)):
#             if user_input[index] == user_input[len(user_input) - index - 1]:
#                 print("they match ")
#                 # user_input = user_input - 1
# # return 

# print(check_palindrome())
import string
def check_anagram(word1, word2):
    word1 = word1.replace(" ", "")
    word2 = word2.replace(" ", "")
    word1 = sorted(word1.lower())
    word2 = sorted(word2.lower())
    
    if word1 == word2:
        print("True")
    else:
        print("False")
check_anagram("a bc", "acB")
