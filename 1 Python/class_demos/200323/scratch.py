counter = 0
output = ''
while counter < 10:
    output = 'a' + output + 'bb' #changed
    counter = counter + 2
print(output)


'''
while True:
    user_input = input("Please type cat: ")
    if user_input == 'cat':
        break
'''

'''
pieces = ''
for piece in ['a', 'b', 'c', 'd', 'e']:
    pieces = pieces + piece
    print(f"The letters are {pieces}")
'''
'''
while True:
    # paste code here
    var1 = input("Please type cat >")
    if var1 == 'cat':
        break
'''

'''
abc_counter = ''
for piece in 'abcde':
    abc_counter = abc_counter + piece + ', '
print(abc_counter)
'''
'''
a_num = input("How many a's do you want? ")
a_num = int(a_num)
pieces = list(range(a_num))
output = ''
for piece in pieces:
    output = output + 'a'
print(output)
'''



'''
# scratch.py

while True:
    user_response = input("Should I print a? ")
    if user_response == 'yes':
        print('a')
    if user_response == 'no':
        break
print('done')
'''