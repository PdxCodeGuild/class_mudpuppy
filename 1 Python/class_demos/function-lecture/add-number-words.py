# based on written_addition.py

# What is wrong with this code?
# What sticks out and bothers you about it?

number_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}

valid_input = False
while not valid_input:
    num1 = input("Spell out a number with letters: ")
    if num1 in number_dict:
        valid_input = True
    else:
        print(f"{num1} is not supported. Try entering a different number: ")


valid_input = False
while not valid_input:
    num2 = input("Spell out a number with letters: ")
    if num2 in number_dict:
        valid_input = True
    else:
        print(f"{num2} is not supported. Try entering a different number: ")

num1_int = number_dict[num1]
num2_int = number_dict[num2]

number_sum = num1_int + num2_int

print(f"The sum is {number_sum}")