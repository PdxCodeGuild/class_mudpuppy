#Average numbers lab version 2 March 24th, 2020

input_nums = []

while True:
    user_input = input("Next number, or 'done': ")

    if user_input == 'done':
        break
    input_nums.append(int(user_input))

run_sum = 0
for num in input_nums:
    run_sum = run_sum + num

num_avg = run_sum / (len(input_nums))

print(f'The average of your numbers is {num_avg}')