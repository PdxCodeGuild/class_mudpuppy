with open('contacts_example.csv', 'r') as f:
    lines = f.read().strip().split('\n')
    # print(lines)
keys = lines[0].split(',')
values = lines[1:] #rename variable
# print(keys)
# print(values)
attribute_list = []
for line in values:
    contacts_dict = {}
    line = line.split(',')
    # print(line)
    for index in range(3):
        key = keys[index]
        trait = line[index]
    # for index, trait in enumerate(line):
        key = keys[index]
        values = trait
        # print(trait)
        contacts_dict[key] = trait 
        print(contacts_dict)
    attribute_list.append(contacts_dict)
print(attribute_list)
while True:
    user_input = input("(C)reate, (R)etrieve, (U)pdate, (D)elete, (Q)uit")
    if user_input == "C":
        new_contact = {}
        user_name = input("What's the user's name? ")
        new_contact['name'] = user_name
        # new_contact['name'] = user_name + 'abc'
        attribute_list.append(new_contact)
        print(attribute_list)
    if user_input == "R":
        user_input = input("Choose (n)ame, (f)ood, (h)obby, or (d)one: ")
        if 'n' == user_input:
            user_name = input("Give me a name: ")
            for input_dict in attribute_list:
                if user_name == input_dict['name']:
                    print(input_dict)
        if 'f' == user_input:
            user_food = input("Give me a food: ")
            for input_dict in attribute_list:
                # print(input_dict['food'], user_food)
                if user_food == input_dict['food']:
                    print(input_dict)
                # if input_tup[0] == user_food:
                #     print(input_tup)
        elif 'h' == user_input:
            user_hobby = input("Give me a hobby: ")
            for input_dict in attribute_list:
                if user_hobby == input_dict['hobby']:
                    print(input_dict)
        elif 'd' == user_input:
            break

    elif user_input == "U":
        user_update = input("Choose a name to change ")
        for contacts_dict in attribute_list:
            if contacts_dict['name'] == user_update:
                new_hobby = input("Choose a new hobby ")
                contacts_dict['hobby'] = new_hobby
    elif user_input == "D":
        user_delete = input("Choose a name to delete ")
        for contacts_dict  in attribute_list:
            if contacts_dict['name'] == user_delete:
                attribute_list.remove(contacts_dict)
        print("Updated Dictionary:", attribute_list)         
    elif user_input == "Q":
        break
print(attribute_list)