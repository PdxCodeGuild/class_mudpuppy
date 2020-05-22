class NumList:
    def __init__(self):
        self.nums = []

    def append(self, in_num):
        self.nums.append(int(in_num))

    def average(self):
        return sum(self.nums)/len(self.nums)

nl = NumList()
while True:
    user_input = input("Enter a number (or 'done'): ")
    if user_input == 'done':
        break
    nl.append(user_input)

print(nl.nums)
print(nl.average())
