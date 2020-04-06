
def _main_():
    """ Ask's if you would like to check palindrome or anagram """
    while True:
        c = input("Enter palindrome, anagram, im done: ") # maybe just do .lower() once on this line after input
        if c.lower() == "im done":
            print("Thank You! ")
            break
        if c.lower() == "palindrome":
            text = input("Enter a word: ")
            print(check_palindrome(text))
        elif c.lower() == "anagram":
            word1 = input("Enter the first word: ")
            word2 = input("Enter the second word: ")
            print(check_anagram(word1, word2))

def flip_text(text):
    """ Flips inputed text. """
    output = ''
    for char in text:
        output = char + output
    return output
# I like the way you did this, you could use text[::-1] or ''.join(reversed(text))
# You can also use .replace with text here to remove punctuation
def remove_vowels(text):
    for vowel in 'aoeui':
        text.replace(vowel, '')
    return text

def check_palindrome(text):
    """ Checks if a word is a palindrome. """
    if flip_text(text) == text:
        return f'{text} is a palindrome!'
    return f'{text} is not a palendrome!'

def check_anagram(word1, word2):
    """ Checks if two words have the same letters. """
    w1 = word1.lower().replace(" ", "")
    sorted1 = sorted(w1)
    w2 = word2.lower().replace(" ", "")
    sorted2 = sorted(w2)
    if sorted1 == sorted2:
        return f"{word1} and {word2} are anagrams!"
    return f"{word1} and {word2} are not anagrams!"

_main_()
