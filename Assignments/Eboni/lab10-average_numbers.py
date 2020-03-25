"""
We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember len will give you the length of a list.

The code below hows how to loop through an array, and prints the elements one at a time.
"""


nums = [5, 0, 8, 3, 4, 1, 6]
for num in nums:
    print(num)
    number_sum = sum(nums)
print(number_sum)
number_average = number_sum/len(nums)
print(number_average)