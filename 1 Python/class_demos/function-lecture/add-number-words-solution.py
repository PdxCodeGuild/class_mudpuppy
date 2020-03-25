def get_valid_input():
    valid_input = False
    while not valid_input:
        num1 = input("Spell out a number with letters: ")
        if num1 in number_dict:
            return num1
        else:
            print(f"{num1} is not supported. Try entering a different number: ")


number_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}

num1 = get_valid_input()
num2 = get_valid_input()

num1_int = number_dict[num1]
num2_int = number_dict[num2]

number_sum = num1_int + num2_int

print(f"The sum is {number_sum}")