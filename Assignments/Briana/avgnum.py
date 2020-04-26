# Version 1

# def avg(nums):
#     return sum(nums) / len(nums)

# nums = [5, 0, 8, 3, 4, 1, 6]

# average = avg(nums)
# print(average)

# # OR

# from statistics import mean 

# def avg(nums):
#     return mean(nums)
# nums = [5, 0, 8, 3, 4, 1, 6]
# print(avg(nums))


# Version 2

from statistics import mean
i = 1
nums = []
def avg(nums):
    return mean(nums)
    
while True:

    user_input = input("Enter a bunch of numbers; Type 'done' to calculate average: ")
    if user_input == "done":
        print(avg(nums))
        break
    else:
        nums.append(int(user_input))
        i += 1