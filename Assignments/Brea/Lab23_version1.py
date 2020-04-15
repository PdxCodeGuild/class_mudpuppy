#Lab 23, version 1, April 13th, 2020

import os
print(os.path.abspath(__file__)) #tells me where my file is
BASE_dir = (os.path.dirname(os.path.abspath(__file__)))
csv_file = os.path.join(BASE_dir, 'contacts_example.csv')

with open(csv_file, 'r') as file:
    raw_contacts = file.read().strip().split('\n')
    print(raw_contacts)

contacts_list = []
final_contacts_list = []

for person in raw_contacts:
    person_info = person.split(',')
    contacts_list.append(person_info)

#print(contacts_list)

#for one_list in contacts_list:

for sub_list in contacts_list: 
    contacts_dict = {}    #index here is pointing to a contact sub-list
    for index, category in enumerate(contacts_list[0]):  #goes over indices name, food, hobby
        contacts_dict[category] = sub_list[index] #contacts_list[sub_list[0:3]] #list indices must be slices, not string
    final_contacts_list.append(contacts_dict)

print(final_contacts_list)