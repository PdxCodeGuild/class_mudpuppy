

def flip_text(text):
    output = ''
    for char in text:
        output = char + output
    return output

def check_palindrome(text):
    if flip_text(text) == text:
        print(f'{text} is a palindrome!')
    else:
        print(f'{text} is not a palendrome!')


while True:
    text = input("Enter a word or type im done to exit: ")
    if text.lower() == 'im done':
        print("Thank You.")
        break
    else:
        check_palindrome(text)
