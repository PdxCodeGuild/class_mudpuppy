with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)

# contact_list = ['name, address, phone number', 'Briana, 6755 se 83, (281)386-2111', 'Ayo, 4242 blueberry ln, (800)616-2839', 'Maron, 666 crimson blvd, (503)386-5959', 'Randall, 502 cereal st , (804)282-9999']

contact_list = []

header = lines[0]
keys = lines[1:5]
# print(header)
# print(keys)

header = header.strip().split(',')  

for i in range(1, len(lines)):  

    keys = lines[i].split(',')

    contact = dict(zip(header, keys)) 

    contact_list.append(contact)

# print(len(lines))

####print(contact_list)

# print(header)

# print(keys)


# Implement a CRUD REPL
# Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
user_input = input('Enter name, address, and phone number of contact you\'d like to add: \n ')

keys2 = user_input.split(',') 

print(keys2)

contact2 = dict(zip(header, keys2))

# split keys2
# make into dict
# zip on header
# append onto contact list 

contact_list.append(contact2)

print(contact_list)

# Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information

retrieve = input('Enter contact, attribute, and value of attribute you\'d like to update: \n')

new_entry = retrieve.split(',')
#larissa, address, portland dr
#.get 


#retrieve contact attribute with name and attribute
#insert new attribute

# Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
# Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.