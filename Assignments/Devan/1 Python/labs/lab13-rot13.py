import string as str
import clipboard
from huepy import *
import sys

class Rot13:

    def menu(self):
        try:
            action = input("\nEnter encrypt, decrypt, or done: ")
            if action == 'encrypt':
                rot13.encrypt()
            if action == 'decrypt':
                rot13.decrypt()
            if action == 'done':
                print(bold(yellow("\nThank's for using the cypher.")))
                sys.exit()
            else:
                print('\nNot a valid input. ')
                rot13.menu()
        except KeyboardInterrupt:
            print(bold(yellow("\nThank's for using the cypher.")))

    def encrypt(self):
        text = input('What would you like to encrypt: ')
        encryption = ''
        for letter in text:
            if letter in str.punctuation or letter in str.whitespace:
                encryption += letter
            if letter in str.ascii_lowercase:
                i = str.ascii_lowercase.find(letter) - 13
                encryption += str.ascii_lowercase[i]
            if letter in str.ascii_uppercase:
                i = str.ascii_uppercase.find(letter) - 13
                encryption += str.ascii_uppercase[i]
        print('\nYour encrypted text is: ' + lightgreen(encryption))
        print('\n' + info('The text has been copied to your clipboard'))
        clipboard.copy(encryption)
        rot13.menu()

    def decrypt(self):
        text = input('What would you like to decrypt: ')
        decryption = ''
        for letter in text:
            if letter in str.punctuation or letter in str.whitespace:
                decryption += letter
            if letter in str.ascii_lowercase:
                i = (str.ascii_lowercase.find(letter) + 13) % len(str.ascii_lowercase)
                decryption += str.ascii_lowercase[i]
            if letter in str.ascii_uppercase:
                i = (str.ascii_uppercase.find(letter) + 13) % len(str.ascii_uppercase)
                decryption += str.ascii_uppercase[i]
        print('\nYour decrypted text is: ' + lightgreen(decryption))
        print('\n' + info('The text has been copied to your clipboard'))
        clipboard.copy(decryption)
        rot13.menu()


rot13 = Rot13()

rot13.menu()
