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
    print(final_contacts_list)
    return create_dict

def retrieve_contact(inpt_name):
    found = False
    for dictionary in final_contacts_list:
        if inpt_name == dictionary['name']:
            found = True
            return dictionary
            #print(f"{inpt_name}'s favorite food is {final_contacts_list[]} and their hobby is {final_contacts_list[]}.'")
    print("That user cannot be found in this contact list.")
    return None
    

def update_contact(inpt_name):
        user_input_fh = input(f"Would you like to update {inpt_name}'s food or hobby? : ")

        if user_input_fh == 'food':
            inpt_food = input(f"What is {inpt_name}'s new favorite food? : ")
            for dictionary in final_contacts_list:
                if dictionary['name'] == inpt_name:
                    dictionary['food'] = inpt_food
                    print(final_contacts_list)

        elif user_input_fh == 'hobby':
            inpt_hobby = input(f"What is {inpt_name}'s new hobby? : ")
            for dictionary in final_contacts_list:
                if dictionary['name'] == inpt_name:
                    dictionary['hobby'] = inpt_hobby
                    print(final_contacts_list)
        else:
            print("That is not an option")
        return dictionary

def delete_contact(inpt_name):
    for i in range(len(final_contacts_list)):
        if final_contacts_list[i]['name'] == inpt_name:
            del final_contacts_list[i]
    print(final_contacts_list)
    return inpt_name

while True:
    print("You can print 'done' to end this program.")
    user_input1 = input("Would you like to create, retrieve, update, or delete a record? : ")
   
    if user_input1 == 'done':
        break

    elif user_input1 == 'create':
            user_input2 = input("For whom would you like to create an entry? : ")
            user_input3 = input("What is their favorite food? : ")
            user_input4 = input("What is their hobby? : ")
            create_contact(user_input2, user_input3, user_input4)
    
    elif user_input1 == 'retrieve':
        user_input5 = input("Whose information would you like to retrieve? : ")
        retrieve_contact(user_input5)
    
    elif user_input1 == 'update':
        user_input6 = input("Whose information would you like to update? : ")
        update_contact(user_input6)
        
    elif user_input1 == 'delete':
        user_input7 = input("Whose information would you like to delete? : ")
        delete_contact(user_input7)
        print(f"{user_input7}'s record has been deleted.")

    else:
        print("Sorry, try again")