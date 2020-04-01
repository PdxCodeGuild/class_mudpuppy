#Lab 15, version 1, March 31st, 2020

user_input = int(input("What whole number (1-99) would you like to convert to words?: "))

ones_dict = {
1: 'one',
2: 'two',
3: 'three',
4: 'four',
5: 'five',
6: 'six',
7: 'seven',
8: 'eight',
9: 'nine'}

teens_dict = {
10: 'ten',
11: 'eleven',
12: 'twelve',
13: 'thirteen',
14: 'fourteen',
15: 'fifteen',
16: 'sixteen',
17: 'seventeen',
18: 'eighteen',
19: 'nineteen'}

tens_dict = {
2: 'twenty',
3: 'thirty',
4: 'forty',
5: 'fifty',
6: 'sixty',
7: 'seventy',
8: 'eighty',
9: 'ninety'}


if user_input < 10:
    output = ones_dict[user_input]
    output = str(output)
    print(f"Your number in words is {output}")

elif user_input > 9 and user_input < 20:
    output = teens_dict[user_input]
    output = str(output)
    print(f"Your number in words is {output}")

elif user_input > 19 and user_input < 100:
    tens_dig = user_input // 10
    ones_dig = user_input % 10
    print(f"Your number in words is {tens_dict[tens_dig]}-{ones_dict[ones_dig]}")

if user_input < 1 or user_input > 99:
    print("That number is not accepted")

