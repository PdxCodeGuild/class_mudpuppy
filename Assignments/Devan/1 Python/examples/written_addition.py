# written_additon.py

# collect two numbers from user in letter format
num1 = input('Spell out a number with letters: ')
num2 = input('Spell out a number with letters: ')

# point letter input to number using dictionary
number_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

# add the two number together
number_sum = number_dict[num1] + number_dict[num2]
print(f'The sum is {number_sum}')
