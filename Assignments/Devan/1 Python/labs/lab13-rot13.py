alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_rotated = 'nopqrstuvwxyzabcdefghijklm'

def encrypt(text):
    encryption = ''
    for letter in text:
        i = alphabet.find(letter)
        encryption += alphabet_rotated[i]
    return encryption

def decrypt(text):
    decryption = ''
    for letter in text:
        i = alphabet_rotated.find(letter)
        decryption += alphabet[i]
    return decryption

print(encrypt(input('What would you like to encrypt? ')))
