# Let's build a program to manage a list of contacts. 
# To start, we'll build a CSV ('comma separated values') together, and go over how to load that file. 
# Headers might consist of name, favorite fruit, favorite color. Open the CSV, convert the lines of 
# text into a list of dictionaries, one dictionary for each user. 
# The text in the header represents the keys, the text in the other lines represent the values.

# with open('contacts.csv', 'r') as file:
#     lines = file.read().split('\n')
#     print(lines)

# contacts = [
#     {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
#     {'name':'sam', 'favorite fruit':'pineapple' ...}
# ]

# #Version2 

# Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
# Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
# Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
# Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.

# #Version3 

# When REPL loop finishes, write the updated contact info to the CSV file to be saved.
# I highly recommend saving a backup contacts.csv because
# you likely won't write it correctly the first time.





# HINTS 
# detangle_book.py
# filename = 'story_weird_format.txt' # the file to open
# l1 = [] # we'll put words in here
# l2 = [] # we'll put words in here
# with open(filename, 'r') as f: # f is the file
#     book_str = f.read()
#     book_lst = book_str.strip().split('\t') # remove white space and split on tab
#     for word in book_lst:
#         pairs = word.split(':')
#         if pairs[0] == 'l1':
#             l1.append(pairs[1])
#         else:
#             l2.append(pairs[1])
#         # if the string start with l1
#             # append word to l1
# print(l1, l2)


   
# list_to_dict.py
# start_list = [['a', 'b', 'c'], ['d', 'e', 'f']]

# output = []
# for one_list in start_list:
#     # one_list = ['a', 'b', 'c']
#     print(one_list)
#     one_dict = {}
#     for index in [0, 1, 2]:#range(len(one_list)):
#         #index = 0
#         #one_list[index] = 'a'
#         one_dict[index] = one_list[index]
#     # one_dict = {0: 'a', 1: 'b', 2: 'c'}
#     output.append(one_dict)

# print(output)
# # [{0: 'a', 1: 'b', 2: 'c'}, {0: 'd', 1: 'e', 2: 'f'}]
# '''
# endgoal = [
#     {0: 'a',
#     1: 'b',
#     2: 'c'},
#     {0: 'd',
#     1: 'e',
#     2: 'f'}
# ]
# print(endgoal)
# '''

	# l1:I	l2:green	l1:do	l2:eggs




#BASIC CONTACT LIST 
print("would you like to add a new contact to your list? ")
ans = input("Yes or No?")

#now this here will help with creating and adding the contact to the list.

contact_data = []
while ans == "yes":
    print("Enter the information ")
    name = input("please enter the name here: ")
    phone = input("please enter the phone number here: ")
    email = input("please enter an email address: ")
    if len(phone) != 10: 
        phone = input("There are not enough digits in this number. Please re-enter the number:  ")
    contact = []+[name]+[phone]+[email]
    contact_data.append(contact)
    ans = input("Is there any additional contact information you would like to add: ")
    if ans == "no": 
        break
    if ans == "yes":
        print("Okay")
        
print (contact_data)