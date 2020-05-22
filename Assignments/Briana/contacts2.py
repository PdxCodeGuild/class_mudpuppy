with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)


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


user_input = input('Enter name, address, and phone number of contact you\'d like to add: \n ')

keys2 = user_input.split(',') 

# # print(keys2)

contact2 = dict(zip(header, keys2))


contact_list.append(contact2)

print(contact_list)


# contact_list = list(contact_list.items())

# while True:
#     user_word = input('Enter name of contact you\'d like to retreive: ')
#     for name in contact_list:
#         if name['name'] == user_word:
#             print(name)
#             print(name['name'])

while True:

    user_word = input('Enter name of contact you\'d like to retreive: ')
    for dictionary in contact_list:
        if dictionary['name'] == user_word:
            print(dictionary)
            print(dictionary['name'])

            update_attribute = input('Which attribute would you like to update? ') 

            new_attribute = input('What new value for this attribute would you like to set for ' + user_word + '? ')
            dictionary[update_attribute] = new_attribute
            print(dictionary)
            print(new_attribute)
            print(contact_list)


        delete_contact = input('Which contact would you like to delete: ')

        # if dictionary['name'] == delete_contact:
        #     # contact_list.pop(dict(dictionary))
        #     # del contact_list[dictionary]
        #     print(contact_list)
        #     break
        # contact_list.pop(dictionary)
        # print(contact_list)

        # if dictionary['name'] == delete_contact:
        #     del contact_list[dictionary]
        #     break

        res = [i for i in contact_list if not (i['name'] == delete_contact)] 
        print(res)
