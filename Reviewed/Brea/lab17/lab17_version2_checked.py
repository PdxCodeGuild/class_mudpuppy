#Lab 17, Version 2 Anagram

def split(word):
    return list(word)
# good practice, but generally don't make a function
# that calls a single function, especially one that's already well-known like list()

def remove_spaces(str):
    new_str = ''
    for i in range(len(str)):
        if(str[i] != ' '):
            new_str += str[i]
    return new_str
# I like that you did this the hard way (you learn more that way)
# but you could just do str.replace('', ' ')
# Also, don't use the parameter str, that overwrites a builtin function

user_input1 = input("What is the first input you'd like to compare? : ")
user_input1 = user_input1.lower()

list_inp1 = split(remove_spaces(user_input1))

user_input2 = input("What is the second input to compare? : ")
user_input2 = user_input2.lower()

list_inp2 = split(remove_spaces(user_input2))

list_inp1.sort()
list_inp2.sort()

if list_inp1 == list_inp2:
    print("These two inputs are anagrams!")
else:
    print("These two inputs are not anagrams!")

# Nice!



