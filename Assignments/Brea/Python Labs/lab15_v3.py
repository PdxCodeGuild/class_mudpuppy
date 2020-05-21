#Lab 15, version 3

user_input = int(input("What whole number (1-999) would you like to convert to Roman Numerals?: "))

ones_dict = {
0: '',
1: 'I',
2: 'II',
3: 'III',
4: 'IV',
5: 'V',
6: 'VI',
7: 'VII',
8: 'VIII',
9: 'XI'}

tens_dict = {
1: 'X',
2: 'XX',
3: 'XXX',
4: 'XL',
5: 'L',
6: 'LX',
7: 'LXX',
8: 'LXXX',
9: 'XC'}

hunds_dict = {
1: 'C',
2: 'CC',
3: 'CCC',
4: 'CD',
5: 'D',
6: 'DC',
7: 'DCC',
8: 'DCCC',
9: 'CM'}


if user_input < 10:
    output = ones_dict[user_input]
    output = str(output)
    print(f"Your number in words is {output}")

elif user_input > 9 and user_input < 100:
    tens_dig = user_input // 10
    ones_dig = user_input % 10
    print(f"Your number in words is {tens_dict[tens_dig]}{ones_dict[ones_dig]}")

elif user_input > 99 and user_input < 1000:
    hunds_dig = user_input // 100
    tens_dig = (user_input % 100) // 10
    ones_dig = user_input % 10
    print(f"Your number in words is {hunds_dict[hunds_dig]}{tens_dict[tens_dig]}{ones_dict[ones_dig]}")

elif user_input < 1 or user_input > 999:
    print("That number is not accepted")