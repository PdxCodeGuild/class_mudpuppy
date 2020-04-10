"""
Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.
Hint: you can use modulus to extract the ones and tens digit.
"""
english_dict_ones = {0: '', 1: 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten'  }
english_dict_tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety' }
english_dict_teens = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen' }
english_dict_hundreds = {1: 'one hundred', 2: 'two hundred', 3: 'three hundred', 4: 'four hundred', 5: 'five hundred', 6: 'six hundred', 7: 'seven hundred', 8: 'eight hundred', 9: 'nine hundred' }

input_num = int(input("choose a number "))
hundreds_digit = input_num // 100
tens_digit = (input_num % 100) // 10
ones_digit = input_num % 10

if input_num <= 999:
    print(f"{english_dict_hundreds[hundreds_digit]} {english_dict_tens[tens_digit]} {english_dict_ones[ones_digit]} ")

