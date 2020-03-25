'''
Lab 10: Average Numbers

Version 1

We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember len will give you the length of a list.

Version 2

Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. The following code demonstrates how to add an element to the end of a list.
'''

# create an empty list for numbers
num_list = []

# loop unti user enters done and add input to num_list
while True:
    user_num = input('Enter a number, or done: ')
    if user_num == 'done':
        break
    num = float(user_num)
    num_list.append(num)

# add up all the entered numbers
running_sum = 0
for num in num_list:
    running_sum += num

# get the average
avg = running_sum / len(num_list)

# print out total
print(f'Your total is {running_sum}')

# print out average
print(f'Your average is {avg}')
