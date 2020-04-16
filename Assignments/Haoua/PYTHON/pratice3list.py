'''problem 1: Write a function using random.randint to generate an index, use that index to pick a random element of a list and return it.'''
# import random

# def myfunc():
#     moods = ["happy", "sad", "chill", "sleepy", "romantic", "cozy", "hungry", "manic"]
#     length = len(moods)
#     range1= random.randint(0,length)
#     return moods[range1]
# print(myfunc())

'''problem2'''

# def myfunc():
#     user_list = []
#     user = str(input("Please Enter number or done : "))
#     user_list.append(user)

#     while True:
#         # user = (input("Please enter number or done: "))
#         if user != "done":
#             user = (input("Please enter number or done: "))
#             user_list.append(user)

    
#         if user == "done":
#         # user_list.append(user)
#             length  = len(user_list)-1
#             return user_list[0:length]
#             break
    
# print(myfunc())

'''problem3 Write a function that takes a list of numbers, and returns True if there is an even number of even numbers'''
# def myfunc():
#     list1 = []
#     even_list = []
#     i = 0

#     user = int(input("How many numbers would you like to enter? : "))

#     while i < user:
#         user2 = int(input("Enter a number : "))
#         list1.append(user2)
#         i += 1

#         if user2%2 == 0:
#             even_list.append(user2)

#     length = len(even_list)
        

#     if length%2 == 0:
#         return True
#     else:
#         return False

# print(myfunc())








'''problem4: Print out every other element of a list, first using a while loop, then using a for loop.'''
# list1 = []
# i = 0
# user = int(input("How many numbers would you like to add? :"))

# while i < user:
#     user2 = int(input("Enter a number : "))
#     list1.append(user2)
#     i += 1
# print(list1[0::2])

# list1 = []
# i = 0
# user = int(input("How many numbers would you like to add? :"))

# for i in range(user):
#     user2 = int(input("Enter a number : "))
#     list1.append(user2)
#     i += 1
# print(list1[0::2])

'''problem5:Write a function that returns the reverse of a list:'''
# def myfunc():
#     list1 = []
#     user = int(input("How many numbers would you like to add? : "))
#     i = 0

#     for i in range(user):
#         user2 = input("Enter a number : ")
#         list1.append(user2)
#         i += 1
#     return list1[::-1]
# print(myfunc())

'''problem 6: Write a function to move all the elements of a list with value less than 10 to a new list and return it.'''
# def myfunc():
#     list1 = []
#     og_list = []

#     user = int(input("How many numbers would you like? :"))
#     i = 0

#     while i < user:
#         user2 = int(input("Enter a number : "))
#         list1.append(user2)
#         og_list.append(user2)
#         i += 1
    

#         list2 = sorted(ele for ele in list1 if ele >= 10)
#         # og_list2 = sorted(ele for ele in og_list if ele < 10)
    
#     return f'New list: {list2} Old list {list1}'
  
# print(myfunc())
'''lab 7: Write a function to find all common elements between two lists'''
# def myfunc():
#     list1 = []
#     list2 = []
#     i = 0
#     b = 0
#     user = int(input("How many numbers would you like to add? :"))

#     while i < user:
#         user1 = int(input("Enter a number"))
#         list1.append(user1)
#         i += 1
#     while b < user:
#         user2 = int(input("Enter a number for your second list :"))
#         list2.append(user2)
#         b += 1
#     n_list1 = sorted(ele for ele in list1 if ele in list2)

#     return (n_list1)
# print(myfunc())
'''lab 8: Write a function to combine two lists of equal length into one, alternating elements.'''
# list1 = []
# list2 = []
# i = 0
# b = 0

# user = int((input("How many items in the list?")))
# # print(type(user))
# # user2 = input("Add item to your first list : ")
# # # 
# while i < user:
#     user2 = input("Add item to your first list : ")
#     i += 1
#     # list1.append(user2)
#     if user2.isdigit():
#         nuser2 = int(user2)
#         list2.append(nuser2)
#     else: 
#         nnuser2 = str(user2)
#         list1.append(nnuser2)

# while b < user:
#     user3 = input("Add item to your second list : ")
#     b += 1
#     if user3.isdigit():
#         nuser3 = int(user3)
#         list2.append(nuser3)
#     else:
#         nnuser3 = str(user3)
#         list1.append(nnuser3)




# def countList(list1, list2): 
#     return [sub[ele] for ele in range(len(list2)) 
#                       for sub in [list1, list2]] 
# print(countList(list1, list2))    


'''lab 9: Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number'''
user = int(input("How many numbers would you like to check? : "))
list1 = []
i = 0
target = 7

while i < user:
    user2 = int(input("Enter a number : "))
    list1.append(user2)
    i += 1
def counter_1(list1):
    return [ele for ele in list1 if ele + ele == target]
print(counter_1(list1))
print(list1)