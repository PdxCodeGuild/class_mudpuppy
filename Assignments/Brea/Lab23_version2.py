#Lab 23, version 2, April 14th, 2020
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

for sub_list in contacts_list: 
    contacts_dict = {}    #index here is pointing to a contact sub-list
    for index, category in enumerate(contacts_list[0]):  #goes over indices name, food, hobby
        contacts_dict[category] = sub_list[index] #contacts_list[sub_list[0:3]] #list indices must be slices, not string
    final_contacts_list.append(contacts_dict)

print(final_contacts_list)

def create_contact(inpt_name, inpt_food, inpt_hobby):
    create_dict = {}
    create_dict['name'] = inpt_name
    create_dict['food'] = inpt_food
    create_dict['hobby'] = inpt_hobby

    final_contacts_list.append(create_dict)
    return create_dict

# def retrieve_contact():
#     pass
#     return pass

# def update_contact():
#     return pass

def delete_contact(inpt_name):
    for i in range(len(final_contacts_list)):
        if final_contacts_list[i]['name'] == inpt_name:
            del final_contacts_list[i]
    return inpt_name

while True:
    print("You can print 'done' at any time to end this program.")
    user_input1 = input("Would you like to create, retrieve, update, or delete a record? :")
   
    if user_input1 == 'done':
        break

    if user_input1 == 'create':
        user_input2 = input("What is the new contact's name? : ")

        if user_input2 == 'done':
            break

        user_input3 = input("What is the new contact's favorite food? : ")
        if user_input3 == 'done':
            break

        user_input4 = input("What is the new contact's hobby? : ")
        if user_input4 == 'done':
            break

        create_contact(user_input2, user_input3, user_input4)
        print(final_contacts_list)
    
    if user_input1 == 'retrieve':
        user_input5 = input("Whose information would you like to view? : ")
        
        if user_input5 == 'done':
            break
        retrieve_contact(user_input5)
        print(final_contacts_list)
    
    if user_input1 == 'update'
        user_input6 = input("Whose information would you like to update? : ")
        
        if user_input6 == 'done':
            break

        user_input7 = input(f"What attribute of {user_input5}'s information would you like to update? :")
            if user_input7 == 'done':
                break

        user_input8 = input(f"What is {user_input5}'s new {user_input6}? : ")
            if user_input8 == 'done':
                break
            
        update_contact(user_input6, user_input7, user_input8)
        print(final_contacts_list)

    if user_input1 == 'delete':
        user_input9 = input("Who's information would you like to delete from the contact list? : ")
        if user_input9 == 'done':
            break

        delete_contact(user_input9)
        print(f"{user_input9}'s record has been deleted.")
        print(final_contacts_list)
