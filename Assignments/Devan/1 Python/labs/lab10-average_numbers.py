'''
We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember len will give you the length of a list.
'''


nums = [5, 0, 8, 3, 4, 1, 6]

running_sum = 0
for num in nums:
    running_sum += num

avg = running_sum / len(nums)

print(running_sum)

print(f'The average is {avg}')
