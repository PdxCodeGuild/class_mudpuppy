# cvc_finder.py
# from string import ascii_lowercase
import string
vowel_string = 'aoeuiy' # points at all vowels
consonant_string = '' # eventually points at all consonants
for letter in string.ascii_lowercase:
    if letter not in vowel_string: # if the letter is not a vowel
        consonant_string += letter # add consonant to string

input_string = 'abcadeemonqrs' # arbitrary input
for index in range(1,len(input_string)-1): # start at 1, go to 1 less than end
    left_side = input_string[index-1]
    middle = input_string[index]
    right_side = input_string[index + 1]
    if (middle in vowel_string and
    left_side in consonant_string and
    right_side in consonant_string): # looking left and right
        ''' if the left is a consonant and the middle
        is a vowel and the right is a consonant'''
        print(left_side + middle + right_side)
        # print(input_string[index-1:index+2])
        # print(input_string[index-1] + input_string[index] + input_string[index + 1])