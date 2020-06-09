with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

list_of_lines = []
for line in lines:
    line = (line.split(",")) # makes our contact file nice and neat

    list_of_lines.append(line) #

headers = list_of_lines[0] #
other_lines = list_of_lines[1:] # 1: starts at the second item on the list not the 0

contacts = []
for line in other_lines:
    contact_dict = {}
    for index, item in enumerate(line): 
        contact_dict[headers[index]] = item 
    contacts.append(contact_dict) 
print(contacts)

while True:
    user_choice = input("Choose (c)reate, (r)etrieve, (u)pdate, (d)elete, (q)uit: ")
    if 'r' == user_choice:
        name_choice = input("Enter the name you chose: ")
        found = False
        for contact in contacts:
            if contact["name"] == name_choice: # will show name choice if they are in contacts
                print(contact)
                found = True       
        if found == False:
            print(f"{name_choice} is not in contacts.") 
            
    elif 'q' == user_choice:
        break

    if 'u' == user_choice:
        name_choice = input("Enter the name you chose: ")
        for contact in contacts:
            if contact["name"] == name_choice: # print the contact name if the contact name is the same as the name choice
                key = input("name? food? hobby? ")
                value = input("What fo you want to change? ")
                contact[key] = value # the end updated
    
    if 'd' == user_choice:
        name_choice = input("Which name would you like to delete? ")
        for contact in contacts: 
            if contact["name"] == name_choice:
                contacts.remove(contact)
                print(f"You deleted {name_choice}")

    if 'c' == user_choice:

        name_choice = input("Which name would you like to add? ")
        food_choice = input(f"What is {name_choice} favorite food?? ")
        hobby_choice = input(f"What is {name choice}  favorite hobby? ")
        
        contact_dict = { 
            'name': name_choice, 
            'food': food_choice,
            'hobby': hobby_choice,
        }
        contacts.append(contact_dict)

print(contacts)
