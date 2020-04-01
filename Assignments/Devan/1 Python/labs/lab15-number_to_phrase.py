

# Define our dicts of numbers in text form
singles = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', \
           7: 'Seven', 8: 'Eight', 9: 'Nine'}
teens = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
         15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']


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


num = int(input("Please enter a number: "))

if num < 100:
    print(f"Your number is {tens_text(num)}")
elif num < 1000:
    print(f"Your number is unknown")
