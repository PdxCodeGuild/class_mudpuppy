#lab20-credit_card_validation.py

nums = "4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5".split()
print(nums)

int_list= []

for num in nums:
    int_list.append(int(num))
#Convert the input string into a list of ints

check = int_list.pop(-1)
# Slice off the last digit. That is the check digit

int_list_reverse = int_list[::-1]
# Reverse the digits

for index, num in enumerate(int_list_reverse):
# Print(index, num, index % 2 == 0)

    if index % 2 == 0:
        int_list_reverse[index] = num * 2

# Double every other element in the reversed list

for index, num in enumerate(int_list_reverse):
    if num > 9:
        int_list_reverse[index] = num - 9
# Subtract nine from numbers over nine

sum = sum(int_list_reverse)
# Sum of all numbers

if sum % 10 == check:
    print("valid")
Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid

print(int_list_reverse)