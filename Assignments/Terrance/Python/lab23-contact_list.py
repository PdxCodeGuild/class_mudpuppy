#lab23-contact_list.py

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

#Once you've processed the file, your list of contacts will look something like this...

list_of_lines = []
for line in lines:
    line = (line.split(",")) # splits the line by commas
    list_of_lines.append(line) # appends lines to the list of lines

headers = list_of_lines[0] # gets the list of lines (header) at the first index
other_lines = list_of_lines[1:] # gets ever line after the first line or header

contacts = []
for line in other_lines:
    contact_dict = {} # creates a dictionary for the contact list
    for index, item in enumerate(line): # item in the line
        contact_dict[headers[index]] = item # creating the key - value pair in the dictionary
    contacts.append(contact_dict) # adds the contact to the contact dictionary

print(contacts)

while True:
    user_choice = input("Choose (c)reate, (r)etrieve, (u)pdate, (d)elete, (q)uit: ")
    if 'r' == user_choice:
        name_choice = input("Enter the name you chose: ")
        found = False
        for contact in contacts:
            if contact["name"] == name_choice: # print the contact name if the contact name is the same as the name choice
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
                key = input("name, food, hobby: ")
                value = input("What is your change? ")
                contact[key] = value # this is where the change is made
    
    if 'd' == user_choice:
        name_choice = input("Which name would you like to delete: ")
        for contact in contacts: 
            if contact["name"] == name_choice:
                contacts.remove(contact)
                print(f"We removed {name_choice}")

    if 'c' == user_choice:

        name_choice = input("Which name would you like to add: ")
        food_choice = input("What is your favorite food?: ")
        hobby_choice = input("What is your favorite hobby?: ")
        
        contact_dict = { 
            'name': name_choice, 
            'food': food_choice,
            'hobby': hobby_choice,
        }
        contacts.append(contact_dict)

print(contacts)