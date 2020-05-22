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

# def create_contact(inpt_name, inpt_food, inpt_hobby):
#     create_dict = {}
#     create_dict['name'] = inpt_name
#     create_dict['food'] = inpt_food
#     create_dict['hobby'] = inpt_hobby

#     final_contacts_list.append(create_dict)
#     return create_dict

# def retrieve_contact(inpt_name):
#     for dictionary in final_contacts_list:
#         if inpt_name == dictionary['name']:
#             print(dictionary)
#             #print(f"{inpt_name}'s favorite food is {final_contacts_list[]} and their hobby is {final_contacts_list[]}.'")
#         else:
#             print("That user cannot be found in this contact list.")
#     return inpt_name

# print(final_contacts_list[1]['name'])

# def retrieve_contact(inpt_name):
#     for piece in final_contacts_list:
#         if inpt_name == final_contacts_list[piece]:
#             print(piece)
#     return piece

def update_contact(inpt_name):
        user_input7 = input(f"Would you like to update {inpt_name}'s food or hobby? : ")

        if user_input7 == 'food':
            user_input8 = input(f"What is {inpt_name}'s new favorite food? : ") #not sure if I can use user_input8 twice on two lines
            for dictionary in final_contacts_list:
                if dictionary['name'] == inpt_name:
                    dictionary['food'] = user_input8

        if user_input7 == 'hobby':
            user_input8 = input(f"What is {inpt_name}'s new hobby? : ")
            for dictionary in final_contacts_list:
                if dictionary['name'] == inpt_name:
                    dictionary['hobby'] = user_input8
        else:
            print("That is not an option")

        return inpt_name

update_contact('Ben')
print(final_contacts_list)

# def delete_contact(inpt_name):
#     for i in range(len(final_contacts_list)):
#         if final_contacts_list[i]['name'] == inpt_name:
#             del final_contacts_list[i]
#     return inpt_name


