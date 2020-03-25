import operator

def get_valid_input():
    valid_input = False
    while not valid_input:
        num1 = input("Spell out a number with letters: ")
        if num1 in number_dict:
            return num1
        else:
            print(f"{num1} is not supported. Try entering a different number: ")


def reduce_list_to_value(fn, starting_value, values):
    accumulator = starting_value
    for val in values:
        accumulator = fn(accumulator, val)
    
    return accumulator

def square_and_add(x,y):
    return x + y**2

number_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}

numbers = []
for _ in range(4):
    inp = get_valid_input()
    numbers.append(number_dict[inp])


number_sum = reduce_list_to_value(operator.add, 0, numbers)
product = reduce_list_to_value(operator.mul, 1, numbers)
sum_squares = reduce_list_to_value(square_and_add, 0, numbers)

print(f"The sum is {number_sum}, the product is {product}, the sum of squares is {sum_squares}")