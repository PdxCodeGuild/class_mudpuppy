with open('contacts_example.csv', 'r') as f:
    lines = f.read().split('\n')
    print(lines)
keys = lines[0].split(',')
values = lines[1:] #rename variable
print(keys)
print(values)

for line in values:
    contacts_dict = {}
    line = line.split(',')
    print(line)
    for index, trait in enumerate(line):
        key = keys[index]

        print(trait)
        contacts_dict[key] = trait
        print(contacts_dict)
# contacts = []
# for piece in lines:
#     print(piece)








# 
# for index in range(len(name)):
#     index = 0
#     name[index] = 'name'
#     name_dict[index] = name[index]
#     contacts.append(name_dict)
# print(contacts)