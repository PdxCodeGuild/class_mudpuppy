#Test Examples April 6th, 2020

#same_letters.py, compares two lists' indices
# word1 = 'abcde'
# word2 = 'abcdf'
# word1_list = list(word1)
# word2 = list(word2)
# print(word1_list, word2)

# words_are_same = True

# for index in range(len(word1_list)):
#     if word1_list[index] != word2[index]:
#         pass
#     else:
#         words_are_same = False
#     print(words_are_same)

# import string
# abc_list = list(string.ascii_lowercase)
# for num in [0, 3, 25]:
#     print(abc_list[num])

#----------------------------------

#cvc_finder.py, trying to find consonant, vowel, consonant groupings in a given string
# from string import ascii_lowercase
import string

vowel_string = 'aeiouy' #points at all the vowels
consonant_string = ''
for letter in string.ascii_lowercase:
    if letter not in vowel_string: #if letter not in vowel_sting
        consonant_string += letter #add to consonant strung

input_string = 'abcadeemonqrs'

for index in range(1, len(input_string)-1): #starts looking for cvc groupings with index[1] being the first possible index for cvc groups, go to 1 less than end
    left_side = input_string[index-1]
    middle = input_string[index]
    right_side = input_string[index+1]

    if (middle in vowel_string and
    left_side in consonant_string and
    right_side in consonant_string):
    






    # if all([input_string[index] in vowel_string and         
    # input_string[index-1] in consonant_string and           
    # input_string[index+1] in consonant_string]):        #looking left and right
    #     '''if the left is a consonant and the middle is a vowel and the right is a consonant'''
        
        
    #     #print(input_string[index-1:index+2])  #also could be print(input_string[index-1] + input_string[index] + input_string[index + 1])
    
