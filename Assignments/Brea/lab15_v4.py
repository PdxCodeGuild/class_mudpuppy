#Lab 15, version 4, March 31st, 2020
import datetime

user_input = input("What time (##:##) do you want to convert to words?: ")

user_input_datetime = datetime.datetime.strftime(user_input "%I:%M")

hours = user_input_datetime(%l)
print(hours)

hours_dict = {
0: '',
1: 'one',
2: 'two',
3: 'three',
4: 'four',
5: 'five',
6: 'six',
7: 'seven',
8: 'eight',
9: 'nine',
10: 'ten'
11: 'eleven',
12: 'twelve'}

mins_dict = {
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
0: '',
2: 'twenty',
3: 'thirty',
4: 'forty',
5: 'fifty',
6: 'sixty',
7: 'seventy',
8: 'eighty',
9: 'ninety'}

hunds_dict = {
1: 'one hundred',
2: 'two hundred',
3: 'three hundred',
4: 'four hundred',
5: 'five hundred',
6: 'six hundred',
7: 'seven hundred',
8: 'eight hundred',
9: 'nine hundred'}

# def hours_words():
#     return(hours_dict[hours])

# def mins_words:
#     if minutes >
    


# if user_input < 10:
#     output = ones_dict[user_input]
#     output = str(output)
#     print(f"Your number in words is {output}")

# elif user_input > 9 and user_input < 20:
#     output = teens_dict[user_input]
#     output = str(output)
#     print(f"Your number in words is {output}")

# elif user_input > 19 and user_input < 100:
#     tens_dig = user_input // 10
#     ones_dig = user_input % 10
#     print(f"Your number in words is {tens_dict[tens_dig]} {ones_dict[ones_dig]}")

# elif user_input > 99:
#     hunds_dig = user_input // 100
#     tens_dig = (user_input % 100) // 10
#     ones_dig = user_input % 10
#     print(f"Your number in words is {hunds_dict[hunds_dig]} {tens_dict[tens_dig]} {ones_dict[ones_dig]}")

# elif user_input < 1 or user_input > 999:
#     print("That number is not accepted")

# print(f"The time is {hours} hours and {minutes} minutes")