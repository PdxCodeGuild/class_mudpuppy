def get_valid_input():
    valid_input = False
    while not valid_input:
        num1 = input("Spell out a number with letters: ")
        if num1 in number_dict:
            return num1
        else:
            print(f"{num1} is not supported. Try entering a different number: ")


number_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}

numbers = []
for _ in range(4):
    inp = get_valid_input()
    numbers.append(number_dict[inp])


number_sum = 0
for num in numbers:
    number_sum = number_sum + num

print(f"The sum is {number_sum}")