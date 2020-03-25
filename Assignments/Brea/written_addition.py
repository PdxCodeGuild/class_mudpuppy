#written_addition.py

num_1 = input("Spell out a number with letters: ")
num_2 = input("Spell out a number with letters: ")

number_dict = {'one' : 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

num1_int = number_dict[num_1]
num2_int = number_dict[num_2]
num_sum = num1_int + num2_int

print(f"The sum is {num_sum}")