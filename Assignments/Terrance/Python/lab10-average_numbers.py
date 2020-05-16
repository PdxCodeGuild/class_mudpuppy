#lab10-averagenumbers.py

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