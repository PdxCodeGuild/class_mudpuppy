#lab15-number_to_phrase

user_input = int(input("What is your number? "))

user_dict_tens = {0: 'zero', 1: 'ten', 2: 'twenty', 3: 'thirty',  4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
user_dict_teens = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
user_dict_ones = {0: 'zero', 1: 'one', 2: 'two ', 3: 'three',  4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

tens_digit = user_input//10
ones_digit = user_input%10

if ones_digit == 0:
    print(user_dict_tens[tens_digit])

elif user_input >=11 and user_input <=19:
    print(user_dict_teens[user_input]) 

elif tens_digit == 0:
    print(user_dict_ones[ones_digit])

else:
    ones_str = user_dict_ones[ones_digit]
    tens_str = user_dict_tens[tens_digit]
    print(f"{tens_str}-{ones_str}.")
