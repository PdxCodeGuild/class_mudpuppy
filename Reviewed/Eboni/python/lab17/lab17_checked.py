def check_palindrome():
    user_input = input('word: ')
    # Set True/False flag
    for index in range(len(user_input)):
            if user_input[index] == user_input[len(user_input) - index - 1]: # Check for mismatches, not matches
                # change True/False flag
    # return True/False flag


print(check_palindrome())
import string
def check_anagram(word1, word2):
    word1 = word1.replace(" ", "")
    word2 = word2.replace(" ", "")
    word1 = sorted(word1.lower())
    word2 = sorted(word2.lower())
    
    return word1 == word2:

print(check_anagram("a bc", "acB"))
in1 = 'a bc'
in2 = 'acB'
if check_anagram(in1, in2):
    print("They are anagrams")
else:
    print("They aren't anagrams")

def remove_vowels(in_text): # hint for removing punctuation
    for vowel in 'aoeuiy':
        in_text = in_text.replace(vowel, '')
    return in_text
