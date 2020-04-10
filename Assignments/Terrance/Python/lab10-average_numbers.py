#lab10-averagenumbers.py

# We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember `len` will give you the length of a list.

# The code below shows how to loop through an array, and prints the elements one at a time.
# ```python
nums = [5, 0, 8, 3, 4, 1, 6]

counter = 0
for i in nums:
    counter = counter + i

print(f"{counter}")

print(round(counter/len(nums), ndigits=2))

#print(help(round))

# user_num = int(input("Enter one number at a time. "))
container = []

while True:
    # paste code here
    var1 = input("Please type cat >")
    container.append(var1)
    if var1 == 'cat':
        break

container.remove("cat")
print(container)