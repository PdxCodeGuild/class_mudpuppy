# # dict1 = {
# #     "a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7, "i" : 8, "j" : 9, "k" : 10, "l" : 11, "m" : 12, "n" : 13, "o" : 14, "p" : 15, "q" : 16,  "r" : 17, "s" : 18, "t" : 19, "u" : 20, "v" : 21, "w" : 22, "x" : 23, "y" : 24, "z" : 25
# #     }
# # dict2 = {
# #     "n" : 0, "o" : 1, "p" : 2, "q" : 3, "r" : 4, "s" : 5, "t" : 6, "u" : 7, "v" : 8, "w" : 9, "x" : 10, "y" : 11, "z" : 12, "a" : 13, "b" : 14, "c" : 15, "d" : 16, "e" : 17, "f" : 18, "g": 19, "h": 20, "i": 21, "j": 22, "k": 23, "l" : 24, "m":  25
# #     }
# # def encrypt(message, shift): #function to encrypt
# #     cipher = ""
# #     for letter in message: #for letters in the input
# #         #checking for space
# #         if letter != " ": #checking for space
# #             num = (dict1[letter] + shift) % 26
# #             #looks up the dictionary and adds the shift to the index
# #             cipher += dict2[num]
# #             #looks up the second dictionary for the shifted alphabets and adds them
# #         else:
# #             cipher += " "
# #     return cipher

# # ### FUNCTION TO DECRFYPT THE STRING according to the shift provided.
# # def decrypt(message, shift):
# #     decipher = " "
# #     for letter in message:
# #         #checks for space
# #         if letter != " ":
# #             num = (dict1[letter] - shift + 26) % 26
# #             decipher += dict2[num]
# #         else:
# #             decipher += " "
# # ##DRIVER FUNCTION TO RUN THE PROGRAM
# # def main():
# #     #use upper() function to convert any lowercase characters to upper case
# #     message = input("Enter a message, luv : ")
# #     shift = 13
# #     result = encrypt(message.upper(), shift)
# #     print(result)

# #     message = input("Enter a message, luv: ")
# #     shift = 13
# #     result = decrypt(message.upper(), shift)
# #     print(result)
# # ###EXECUTES MAIN FUNCTION
# # if __name__ == '__main__':
# #     main()


 
#  #rot_13_cap = ["N","O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G"]
# # def translate(phrase):
# #     translation = "" #We want to loop through every letter and if it isn't a vowel we want to leaveit alone
# #     for eng in phrase: #now we can access each individual letter
# #         if phrase.upper() in eng: #checking to see if the letter is inside of this string and if it is then we know its a vowel
# #            #to make it more efficient we can say if letter.lower() then we only have to type out lowercase letters
# #             if phrase.isupper():
# #                 translation = translation.index() + rot_13_cap.index() #"N","O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G"
# #             else:
# #                 translation = translation + "n","o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g"
# #            #It does not keep our upper case syntax
# #         else:
# #             translation = translation + phrase
# #     return translation
# # print(translate(input("Enter a phrase: ")))

# # rot(13)
# # ---------------------------------------

# # '''c (is the cipher txt)
# # c = (x-n)%26 #formula to convert.

# # 26 because we have 26 letters in the alphabet
# # X is the plain txt
# # N is the key

# # 1. Input from the user
# # ----------
# # '''
# # def encrypted(string, s):
# #     cipher = ""
# #     for chr in string:
# #         if chr ==" ":
# #             cipher = cipher + chr
# #         elif chr.upper() in string:
# #             cipher = cipher + chr ((ord(chr) + s - 65) % 26 + 65)
# #             #extracting the order of the character.
# #             #shift is what the user will provide it
# #             #we subtract from 65 because if it is upper case it starts at 65.
# #         else:
# #             cipher = cipher + chr((ord(chr) + s - 97) % 26 + 97)
# #     return cipher


# # txt = (input("enter the text: "))
# # s = int(input("Enter the shift key"))
# # print("The original string is : ", txt)
# # print("the encrypted msg is:" ,encrypted(txt, s))

# # message = input("enter the message: ")
# # #alphabet = "abcdefghijklmnopqrstuvwxyz"
# # alphabet = {
# #     "a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7, "i" : 8, "j" : 9, "k" : 10, "l" : 11, "m" : 12, "n" : 13, "o" : 14, "p" : 15, "q" : 16,  "r" : 17, "s" : 18, "t" : 19, "u" : 20, "v" : 21, "w" : 22, "x" : 23, "y" : 24, "z" : 25
# #     }
# # alphabet_two= {
# #     "n" : 0, "o" : 1, "p" : 2, "q" : 3, "r" : 4, "s" : 5, "t" : 6, "u" : 7, "v" : 8, "w" : 9, "x" : 10, "y" : 11, "z" : 12, "a" : 13, "b" : 14, "c" : 15, "d" : 16, "e" : 17, "f" : 18, "g": 19, "h": 20, "i": 21, "j": 22, "k": 23, "l" : 24, "m":  25
# #     }
# # key = 13
# # encrypt = " "
# # for i in message: #will comvert each value
# #     position = alphabet.find(i) #will search for the string in i and will return the index value
# #     newposition = position + key # add ke valuev to index value take the  new value and store it in here
# #     encrypt += alphabet[newposition] #it will add new character inside encrypt and it will be generated here
# # print(encrypt) #storing the message


# #ROT13 practically provides no security at all 
# #ROT13 = rotate string by 13 positions % 26 (for 26 characters)
# #------------------------------------------------------------
# # '''abc -----------> ?
# #     encrypt
# #     <-----------------
# #     decrypt
# # now we want to find the encrypted characters
# # OR: abcd......z #when we want to encrypt we use m, when we want to decrypt we use the associated string in the original alphabet

# # SIMPLE PYTHON CODE THAT DOES IT.
# # '''
# # '''
# # #1
# # # '''
def rot13(phrase):
    abc = "abcdefghijklmnopqrstuvwxyz"
    # abc2 = "nopqrstuvwxyzabcdefghijkl"
    out_phrase = "" #encrypted string originally empty
    for chr in phrase: #we want to encrypt each character in the phrase
        out_phrase += abc[(abc.find(chr)+13)%26] #we wound find the position at
    return out_phrase
phrase = input("input a phrase or letter: ")
encrypt = print(rot13(phrase))
decrpt = print(rot13(rot13(phrase))) #use rot13 twice to decrypt the code
# '''

# #2.ONE LINER:

# phrase = str(input("input a phrase or letter: "))
# rot = int(input("Enter a rotation: "))
# abc = "abcdefghijklmnopqrstuvwxyz" #we have to define abc
# encrypt = print("".join([abc[(abc.find(c)+{rot})%26] for c in phrase]))
# decrypt = print("".join([abc[(abc.find(c)+{rot})%26] for c in phrase]))

# join empty string
#[abc[(abc.find(c)+13)%26] = expression of list comprehension, executed for every element in the list
# for c in phrase = for every character in phrase we preform the above
# # '''

#3 BUILT IN LIBRARY - CODECS
# import codecs #import the library and call the encode function.
# #codecs handles capitlization for you.
# # if you apply ROT13 to an uppercase letter, it will remain uppercase
# #after enconding. 
# phrase = input("input a phrase or letter: ")
# print(codecs.encode(phrase, 'rot_13')) #the enconde function from the coecs library
# #takes up to three parameters:
# # 1. The first parameter is the string object to encode.
# # 2. 2nd parameter is the encoding scheme (default: 'utf-8')
# # 3. 3rd parameter allows ou to customize error handling. (most cases you can use the default error handling)

# print(codecs.encode(codecs.encode(phrase, 'rot_13'), 'rot_13'))
# '''







# '''
# #WHAT ARE THE APPLICATIONS OF R0T13 ALGORITHM
# '''
# The ROT13 algorithm is easy to decrypt. An attacker can easily crack your code
# by running a probabilistic analysis on the distribution of the letters in your 
# encrypted text. You should never rely on this algorithm to encrypt your messages!

# SO, WHAT ARE THE APPLICATIONS OF "ROT13 Algorithm"

# 1. Obscure potentially offensive jokes in online forums.
# 2. Obscure the result of puzzles in online forums.
# 3. Obscure possible spoilers for movies or books.
# 4. Make fun of existing (weak) encryption algorithms: "56-bit DES is stronger than ROT13"
# 5. Obscure email addresses on websites against not very sophisticated email bots (the 99%)
# 6. Use it as a game to find phrases that make sense in both forms, encrypted or decrypted.
#     example: (png, cat), (be, or)
# 7. ROT13 is a special case of the popular CAESAR CIPHER. 
#    ROT13 serves as an educational tool to explain it.
# '''


# #HOW IS ROT13 RELATED TO THE CAESAR CIPHER?
# '''The caesar cipher is the generalization of the ROT13 algorithm

# ROT does nothing but fix the number of positions down the alphabet to +13.
# original txt = cleartext or plaintext (JARGON)

# WHY 13 and not ANOTHER NUMBER?:
# 1. it ensures that applying the encryption twice returns the original cleartext.
# 2. Allows us not to have to define two separate methods for encryption and decryption - one method to rule them all.
# 3. THIS IS NOT THE CASE FOR ANY OTHER NUMBER: 
#     if we apply ROT5 twice we get ROT10 encryption.
# '''

# #ONLINE TOOL FOR ROT13 ENCRYPTION & DECRYPTION:
# # To encrypt your own cleartext simply replace the string value of the variable "clear_text" 
# # with your personal string,

# abc = "abcdefghijklmnopqrstuvwxyz"
# rot_13 = lambda x: "".join([abc[(abc.find(c)+13)%26] for c in x])


# # encryption
# clear_text = 'cleartext'
# encrypted_text = rot_13(clear_text)
# print('Your encrypted text: ' + encrypted_text)

# # decryption
# decrypted_text = rot_13(encrypted_text)
# print('Your decrypted text: ' + decrypted_text)


# #ALTERNATIVES:
# '''Most ALTERNATIVES are stronger than ROT13. Here are a few:
# 1. Triple DES: 
#     1. replace the original DATA ENCRYPTION STANDARD algorithm
#     2. hackers eventually defeated it with ease. Was the standard at one point
#     3. Triple DES uses three individual keys with 56 bits each. 
#     4. The total key length addds up to 168 bits, 
#         but experts would argue that 112 bits in key strength is better
#     5. Still manages to make a dependable hardware encryption solution for financial services and other industries

# 2. RSA:*****GREAT FOR EMAILS
#     1. RSA is a public-key encryption algorithm
#         and the standard encrypting data sent over the internet.
#     2. one of the methods used in our PGP and GPG programs.
#     3. RSA is considered an asymmetric algorithm due to its use of a pair of keys. 
#         You've got your public key: used to encrypt message
#         You've got your private key: used to decrypt it.
#     4. The result of RSA encryption is a huge batch of mumbo jumbo that takes attackers time and processing power to break.

# 3. BLOWFISH:
#     1. Algorithm designed to replace DES. 
#        This symmetric cipher splits messages into blocks of 64 bits and encrypts them individually
#     2. Great for speed and overrall effectiveness (never been defeated)
#     3. Vendors have taken full advantage of its free availability in the public domain.
#     4. Blowfish can be found in software categories ranging from e-commerce
#         for securing payments to password management tools, where it used to protect passwords.
#     5. More flexible encryption
# 4. TWOFISH
# 5, AES: