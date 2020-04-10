
def sum(numbers):
    run_sum = 0
    for num in numbers:
        run_sum += num

    return run_sum

def average(numbers):
    return sum(numbers) / len(numbers)

input_nums = []

while True:
    user_input = input("Next number, or 'done': ")

    if user_input == 'done':
        break
    input_nums.append(int(user_input))


print(f'The average of your numbers is {average(input_nums)}')