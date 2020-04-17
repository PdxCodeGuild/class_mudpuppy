import string
# #input from user
# # card = int(input("Enter your credit card number: "))

# # card_list = [] #puts card numbers into a list
# # cards_list.append(card)
# # #add each number into the card list
# # card_length = len(card) #gives us how many numbers are in the card

# # check_digit = card.slice([-1]) #removes the last digit of the card

# # card2 = card_list.reverse()
# # double_numbers = card_list[0, 2,]
# # for carrd2:
# #     if card 


# # credit_cards_n

# #redo it as a list

# credit_list = input("enter your credit card number : ")
# length = len(enter)
# eq = length - 1 #equation for removing last digit
# slice_card = enter[0:eq] #prints everything but the last digit
# rev_string = slice_card[::-1] #reverse string
# #use .pop 


# print(rev_string)
# ''' ---------------------------------------------------------------------'''


# str_list = []

# def double_numbers(rev_string):
#     i = 0
#     str = ""
#     str_list.append(str)

#     while i < len(rev_string):
#         str = str+rev_string[i] * ((+ 2))
#         i=i+2        
#     print(str)
# double_numbers(rev_string)

# rev_string2 = int(rev_string)


# #rev_string2 = print(type(typea)) #takes the reverse string and turns it into an integer.

# length = len(rev_string2)
# def sum_values(rev_string2):
#     equation = rev_string2[0] + rev_string2[1] + rev_string2[3]
# # def subtract_nine():
# #     pass
# # #subtract nine from numbers over nine
# # subtract_nine()

# # def sum_values():
user = input("Credit Card Number (seperated each number with spaces): ")

credit_card_list = user.split(" ")

# cclist_1= credit_card_list
exclude = set(string.punctuation) and set(string.ascii_lowercase) and set(string.ascii_uppercase)
user = ''.join(ch for ch in user if ch not in exclude).replace(" ","")
print(user)
print(credit_card_list)

print(len(user))
length = len(user)-1 #because of spaces 

pop = credit_card_list.pop(length)
check_digit = pop

print(pop) #test to make sure pop is being printed, it is.

credit_card_list_global = []

def reverse(credit_card_list):
    return [ele for ele in reversed(credit_card_list)]
rev_cc_list = (reverse(credit_card_list))
print(rev_cc_list)
reverse(credit_card_list)


print(type(credit_card_list))
# print(rev_cc_list)
double_num = []
# def double_numbers(rev_cc_list):
    # double_num = []
for ele in rev_cc_list:
    double_num.append(ele + ele)
        # x *= 2
        # print(
print(double_num)
# print(rev_cc_list)
# double_numbers(rev_cc_list)


# def double(rev_cc_list):
#      return [x * 2 for x in rev_cc_list]
# print(double(rev_cc_list))

# double(rev_cc_list)

# def double_numbers(credit_card_list):
#     i = 0
#     list = []
#     # str_list.append(str)

#     while i < len(user):
#         list =  credit_card_list[i] * (i + 2)
#         i *= 2        
# print(list)
# double_numbers(credit_card_list)

# length = len(user)

# one = cclist_1.pop()
# pri

# i = 0
# for i < len(user):
#     credit_card_list.append(user)



    






    





# len(rev_string)
# print(rev_string[0::)

#rev_string_list = enter.split(" ") #puts the string into a list

# even_numbers = print(rev_string[0, 2, 4, 6, 8, 10, 12, 14, 16, 20 , 22, 24, 26, 28, 30, 32, 34, 38])
# odd_numbers = print(rev_string([1, 3, 5, 7 , 8 , 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37]))
