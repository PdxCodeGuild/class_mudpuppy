from huepy import *

# Define the dict of numbers in text form
singles = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', \
           7: 'Seven', 8: 'Eight', 9: 'Nine'}

teens = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
         15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}

tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']


def _main_():
    """Takes a number, calls functions to convert it to text, then prints the text"""
    while True:
        num = input("Please enter a number or done: ")
        if num == "done":
            print(bold(lightgreen("Thank You!")))
            break
        else:
            try:
                num = int(num)
                if num < 0:
                    num = abs(num)
                    if num < 100:
                        print(f"Your number is negative {tens_text(num)}")
                    elif num < 1000:
                        print(f"Your number is negative {hundreds_text(num)}")
                elif num == 0:
                    print("Your number is zero")
                elif num < 100:
                    print(f"Your number is {tens_text(num)}")
                elif num < 1000:
                    print(f"Your number is {hundreds_text(num)}")
            except Exception:
                print(info(bold("Not a valid input, try again")))


def tens_text(num):
    """Converts an number less than 100 to text"""
    if num < 10:
        return singles[num]
    elif num < 20:
        return teens[num]
    elif num < 100:
        tens_digit = num // 10
        singles_digit = num % 10
        if singles_digit == 0:
            return tens[tens_digit]
        else:
            return tens[tens_digit-2] + ' ' + singles[singles_digit]

def hundreds_text(num):
    """Converts a number between 100 and 1000 to text"""
    hundreds_digit = num // 100
    tens_digit = num % 100
    hundreds_text = singles[hundreds_digit] + ' ' + "Hundred"
    return hundreds_text + ' ' + tens_text(tens_digit)


        # TODO:  Trying to grab the value from the dict and add it to the output string
# def num_to_roman(num):
#     roman_numerals = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
#     roman_num = ''
#     while num > 0:
#         for i in range(num // roman_numerals[key]):
#             roman_num += roman_numerals[value]
#             num -= roman_numerals[key]
#             i += 1
#         return roman_num



_main_()
# num_to_roman(16)
