

singles_and_teens = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', \
                7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', \
                12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', \
                16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}

double_digit = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']


user_input = int(input("Please enter a number: "))
hundreds_digit = user_input // 100
tens_digit = (user_input % 100)//10
ones_digit = user_input % 10


if user_input < 20:
    print(f"Your number is: {singles_and_teens[user_input]}")
elif user_input > 19 < 100:
    print(f"Your number is: {double_digit[tens_digit-2]} {singles_and_teens[ones_digit]}")
elif user_input > 99 < 1000:
    print(f"Your number is: {singles_and_teens[hundreds_digit]} hundred {double_digit[tens_digit-2]} {singles_and_teens[ones_digit]}")
