
def main_menu():
    """ Ask's if you would like to check palindrome or anagram """
    while True:
        user_action = input("Enter palindrome, anagram, im done: ")

    # # IDEA: Take punctuation out of user input
    
        if user_action.lower() == "im done":
            print("Thank You! ")
            break
        if user_action.lower() == "palindrome":
            text = input("Enter a word: ")
            check_palindrome(text)
        elif user_action.lower() == "anagram":
            word1 = input("Enter the first word: ")
            word2 = input("Enter the second word: ")
            check_anagram(word1, word2)

def flip_text(text):
    """ Flips inputed text. """
    output = ''
    for char in text:
        output = char + output
    return output

def check_palindrome(text):
    """ Checks if a word is a palindrome. """
    if flip_text(text) == text:
        print(f'{text} is a palindrome!')
    else:
        print(f'{text} is not a palendrome!')

def check_anagram(word1, word2):
    """ Checks if two words have the same letters. """
    w1 = word1.lower().replace(" ", "")
    sorted1 = ''.join(sorted(w1))
    w2 = word2.lower().replace(" ", "")
    sorted2 = ''.join(sorted(w2))
    if sorted1 == sorted2:
        print(f"{word1} and {word2} are anagrams!")
    else:
        print(f"{word1} and {word2} are not anagrams!")


if __name__ == "__main__":
    main_menu()