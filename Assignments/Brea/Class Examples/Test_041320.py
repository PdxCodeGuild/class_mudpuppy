#Test Examples for April 13th, 2020

#count_double_letters.py

input_string = 'asdfedldieeldcdpwwlmdifnooep'

double_letter_counter = {}

for index in range(len(input_string) - 1):
    active_letter = input_string[index]
    next_letter = input_string[index + 1]
    letter_tup = (active_letter, next_letter)

    if letter_tup in double_letter_counter:
        double_letter_counter[letter_tup] += 1
    else:
        double_letter_counter[letter_tup] = 1

print(double_letter_counter)