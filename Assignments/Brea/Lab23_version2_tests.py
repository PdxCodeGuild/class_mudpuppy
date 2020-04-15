#Lab 23, version 2 function tests

import os
print(os.path.abspath(__file__)) #tells me where my file is
BASE_dir = (os.path.dirname(os.path.abspath(__file__)))
csv_file = os.path.join(BASE_dir, 'contacts_example.csv')

with open(csv_file, 'r') as file:
    raw_contacts = file.read().strip().split('\n')
    print(raw_contacts)

contacts_list = []
final_contacts_list = [{'name': 'Ariana', 'food': 'apples', 'hobby': 'aardvarks'}, {'name': 'Ben', 'food': 'blood oranges', 'hobby': 'biking'}, {'name': 'Chase', 'food': 'cheetos', 'hobby': 'cross-country skiing'}, {'name': 'Diana', 'food': 'dino chicken nuggest', 'hobby': 'dining'}]

# for person in raw_contacts:
#     person_info = person.split(',')
#     contacts_list.append(person_info)

# for sub_list in contacts_list: 
#     contacts_dict = {}    #index here is pointing to a contact sub-list
#     for index, category in enumerate(contacts_list[0]):  #goes over indices name, food, hobby
#         contacts_dict[category] = sub_list[index] #contacts_list[sub_list[0:3]] #list indices must be slices, not string
#     final_contacts_list.append(contacts_dict)

print(final_contacts_list)

def create_contact(inpt_name, inpt_food, inpt_hobby):
    create_dict = {}
    create_dict['name'] = inpt_name
    create_dict['food'] = inpt_food
    create_dict['hobby'] = inpt_hobby

    final_contacts_list.append(create_dict)
    return create_dict

# def retrieve_contact(inpt_name):
#     for 
#         print(f"{inpt_name}'s favorite food is {final_contacts_list[]} and their hobby is {final_contacts_list[]}.'")
#     else:
#         print("That user cannot be found in this contact list.")
#     return inpt_name
# print(final_contacts_list)

def unpdate_contact(inpt_name, inpt_food, inpt_hobby):
    

def delete_contact(inpt_name):
    for i in range(len(final_contacts_list)):
        if final_contacts_list[i]['name'] == inpt_name:
            del final_contacts_list[i]
    return inpt_name

update_contact('Diana')

print(final_contacts_list)
