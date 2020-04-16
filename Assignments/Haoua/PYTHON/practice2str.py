'''problem1'''
# def myfunc():
#     user = str(input("Input a string : "))
#     user2= ''.join([ch*2 for ch in user])
#     return user2

# print(myfunc())


'''problem2'''

'''example:1'''
# def myfunc():
#     list1 = []
#     user = (input("Input a string :"))
    
#     # exclude = set(string.punctuation)
#     # w2 = ''.join(ch for ch in user if ch not in exclude).replace(" ", "")
#     # print(w2)
#     user2 = user.strip()
    
#     list1.append(user2)
#     length = len(user2)
#     i = 0
#     b = -1
#     # list1 = []
#     eq = user2[0:length]
#     # eq = user[0:i]
#     while i < length:
#             word = print(user2[b:length])
#             #list1.append()
#             print(word)
#             print(b)
#             i += 1
#             b += 1
#             list1.append(eq[b:length])
#             continue
#     print(list1)
# myfunc()

'''example 2''' #I was unable to get it to recognize the two different "l"
# user = input("input a string : ")
# user2 = user.strip()
# length = len(user2)-1
# length2 = len(user2)

# def myfunc():
#     i = 0
#     list1 = []

#     while i < length2:
    
#         user2 = user[i]

#         i += 1

#         remove = user.replace(user2, "")
#         list1.append(remove)

#     return list1
# print(myfunc())

'''problem 3: Return the letter that appears the latest in the english alphabet'''
#def myfunc():
    #user = input("Enter a string of characters :")
    #return "The latest letter is " + max(user))
#print(myfunc())
'''problem 4: Write a function that returns the number f occurances of 'hi' in a given string:'''
# def myfunc():
#     user = input("Enter a hi (0-infinite times) : ")
#     i = "hi"
#     count = user.count(i)
#     return user.count(i)

# print(myfunc())
'''problem 5: Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'''
# def myfunc():
#     user = input("Enter cat, dog, or one of each atleast twice (without space) : ")
#     i = "cat"
#     b = "dog"
   
#     cat = user.count(i)
#     dog = user.count(b)
    
#     if dog == cat:
#         return True
#     else:
#         return False

# print(myfunc())

'''problem6: Return the number of letter occurances in a string.'''
# user = input("Check how many times a letter occurs in string: ")
# user2 = input("Which letter would you like to check :")

# def myfunc(user, user2):
#     count1= user.count(user2)
#     return count1
# print(myfunc(user, user2))
'''problem7: Convert input strings to lowercase without any surrounding whitespace.'''
# user = input("Enter a phrase : ").lower()
# user2 = user.strip()
# print(user2)