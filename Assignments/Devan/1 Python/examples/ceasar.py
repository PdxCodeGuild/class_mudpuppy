import string

def  encrypt(string, method):
    output = ""
    for char_code in string.encode('ascii'):
        output += method(char_code)
    return output

def rot13(char_code):
    return chr((char_code + 13 -  97) % 26 + 97)


print(encrypt("abcd", rot13))
