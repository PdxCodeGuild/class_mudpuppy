#Average numbers lab March 24th, 2020

nums = [5, 0, 8, 3, 4 , 1, 6]

run_sum = 0
for num in nums:
    run_sum = run_sum + num
    # print(run_sum)

# for i in range (len(nums)):
#     print(len(nums))

num_avg = run_sum / (len(nums))

print(f'The average of your numbers is {num_avg}')
