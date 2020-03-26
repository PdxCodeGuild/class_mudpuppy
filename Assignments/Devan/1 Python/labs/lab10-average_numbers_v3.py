import operator


# create an empty list for numbers
num_list = []

# loop unti user enters done and add input to num_list
while True:
    user_num = input('Enter a number, or done: ')
    if user_num == 'done':
        break
    num = float(user_num)
    num_list.append(num)


def reduce_list_to_value(fn, starting_value, values):
    accumulator = starting_value
    for val in values:
        accumulator = fn(accumulator, val)
    return accumulator


def add_nums():
    for num in num_list:
        num_list += num
    return


# add up all the entered numbers
number_sum = reduce_list_to_value(add_nums, 0, num_list)

# get the average and sum

avg = number_sum / len(num_list)

# print out average
print(f'Your average is {avg}')

# print out total
print(f'The sum is {number_sum}')
