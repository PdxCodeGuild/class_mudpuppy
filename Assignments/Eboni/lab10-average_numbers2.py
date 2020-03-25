"""
We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember len will give you the length of a list.

The code below hows how to loop through an array, and prints the elements one at a time.
"""


# nums = [5, 0, 8, 3, 4, 1, 6]
# number_sum = 0
# for num in nums:
#     print(num)
#     # number_sum = sum(nums)
#     number_sum = number_sum + num
# print(number_sum)
# print(sum(nums))
# number_average = number_sum/len(nums)
# print(number_average)

"""
Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. The following code demonstrates how to add an element to the end of a list.
"""
nums = []
while True:
    user = input("Enter the numbers ")
    nums.append(user)
    if user == "done":
        break
nums.remove('done')
number_sum = 0
for num in nums:
    print(num)
    number_sum = number_sum + int(num)
print(number_sum)
number_average = number_sum/len(nums)
print(number_average)





