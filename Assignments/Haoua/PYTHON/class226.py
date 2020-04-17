'''
raw strings == [refoxomg a stromg wotj "r" will ignore any escape sequences and interp]
'''
'''
# chr & ord
a_string = "i was wrong about which book dobby dies in, he dies in
another_string = " book 7"
x = 'a' 
print(a*500)
'''

'''
s = 'hello there'

a = s.strip()
b = s.strip('e')
print(a)
print(b)

c = s.split()
print(c)

d = s.split('e')
print(d)

# do not use c style formatting
'''
'''
nums = [3, 'red' , 57, 87, 23, 45, 90, 76, 122, 43, 76, 43, 756]
for each_item in nums: #for each item in the list that I have, print it
    print(each_item)

#check if a list contains an item
print(233 in nums) #in just checks for membership

x = [3,4,5]
t = [3,4,5]
print(nums ==x)
print(t ===x)
print(nums[8::-1])
#you can only use 3 positive integers

list operations
copy() - creates a copy of the list
append() - appends an element to the end of the list
insert() inserts the value at the specified index
remove() - removes the list
pop() - removes the element at the given index
extended() - combines 
'''

i = 0 #flag

while i < 10: #it'll ask 9 questions
    if i == 5:
        break
        # print('woohoo')
    print(i)
    i+= i + 1
else:
    print('i finished normally')
# print('done')
'''
things that are iterable are ranges, lists, strings, sets, dicts, etc. 
'''

'''RANGE FUNCTION
to loop over a range of numbers, we can use range. The value it generates go up to bu tnot inclfuing the number passed as a parameter (here, 10) Each iteration, the variable i will be bound to the values of range.
'''
'''
for i in range (0, len(a)):
    print(i)
'''
'''
my_string = "this is a boring ass string'
for character in my_string:
    print(chr(ord(character)))
'''

fruits = ['apples', 'banonos', 'pears', 'cherries', 'pineapples']

for i in range(len(fruits)):
    if i == 3:
        continue
    print(fruits[i]) #i prints out each element
    #fruits[5] does not exist
print('this is the next line')

'''
How to turn in assignment:
'''
1. pwd
2. mkdir code_guild
3. mkdir code_guild/python
4. ls
5. my blah.py code_guild/python
6. ls
7. cd code_guild/python
8. code blah.py
9. ls blah.py
10. ls -a
NO .GIT IN PYTHON, DESKTOP, OR JAVASCRIPT
THE ONLY PLACE WE SHOULD HAVE .GIT IN PDXCODEGUILD
11. CD ..
12. LS
13.PWD
14.