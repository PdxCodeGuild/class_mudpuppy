#Test Examples, April 8th, 2020

# tup1 = (3 + 5, 4 + 2) #this is a tuple

# vowel_str = 'aeiouy'

# for index, letter in enumerate(vowel_str):
#     print(f"{letter} is at index {index}")

# for index in range(len(vowel_str)): #convert string into something that independently identifies the indices within the string, use len()
#     print(f"{letter} is at index {index}")

list comprehensions
    l1 = []
    for num in range(5):
        l1.append(num * 2)

    l2 = [num*2 for num in range(5)]
    print(l2)

#more about functions
#print('abc', end='def')
#print('abc', 'def', end='\n', sep=' ') #print as usual, \n means move to new line
#print('abc', 'def', end=':\n', sep=';')
#print('a\n\nb') #prints a on one line, prints blank line, prints b on new line

def myprint(*args, sep=' ', end='\n'): # * means the function is going to pack up all the variables in the tuple
    output = ''
    for arg in args[:-1]:  #args[:-1] means that returns list except last thing in the list
        output += arg + sep     #adds a space between each printed letter
        output = output + args[-1] + end    #moves each printed letter to a new line
        print(output, end='')

myprint('a', 'b', 'c')