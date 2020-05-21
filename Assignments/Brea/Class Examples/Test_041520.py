# #Test Examples, April 15th, 2020

# #word_info.py
# import string

# book = "\nSee spot run. Spot runs fast. Run spot, run!\n"
# book = book.strip().lower()
# print(book.split('\n'))

# for punc in string.punctuation:
#     book = book.replace(punc, '')

# book_l = book.split()   #splits book word strings into a line
# word_counter = {}
# for word in book_l:

#     if word in word_counter.keys():    
#         word_counter[word] = word_counter[word] + 1   #increment word (weird syntax), or could be also be  words[word] += 1

#     else:
#         word_counter[word] = 1      #count the word for the first time
        
# print(word_counter)

# #word_info part 2.py--------------------
# word_list = list(word_counter.items())      #creates list of tuples with the word key in index 0, and the counter number in index 1 a las ('see', 1)
# print(word_list)

# while True:
#     user_choice = input("Choose (w)ord, (n)umber, or (d)one : ")

#     if user_choice == 'w':
#         user_word = input("What word would you like to check? : ")      #let them enter a word
#         for word_tup in word_list:      #search the list for the word
#             if word_tup[0] == user_word:  #prints out the words 
#                 word_num = word_tup[0]
#                 print(word_num) #tell them how many times it occurs
    
#     elif user_choice == 'n':
#         user_num = input("Give me the number : ") #let them enter a number
#         for word_tup in word_list:  #search list for that number
#             if word_tup[1] == user_num:
#                 print(word_tup[1])
            
#         #print out word
#     elif user_choice == 'd':
#         break

#     else:
#         print("What do you want?")


# #-----------------
# #how to replace all the vowels in an alphabet string
# # abc = string.ascii_lowercase
# # vowels = 'aeiouy'

# # for vowel in vowels:
# #     abc = abc.replace(vowel, '')    #replacing the vowels in abc string with an empty string ('') which is nothing

# # print(abc)

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

contacts_list = []
final_contacts_list = []

def create_contact(inpt_name, inpt_food, inpt_hobby):
    create_dict = {}
    create_dict['name'] = inpt_name
    create_dict['food'] = inpt_food
    create_dict['hobby'] = inpt_hobby

    final_contacts_list.append(create_dict)
    print(final_contacts_list)
    return create_dict

def retrieve_contact(inpt_name):
    for dictionary in final_contacts_list:
        if inpt_name == dictionary['name']:
            print(dictionary)
            #print(f"{inpt_name}'s favorite food is {final_contacts_list[]} and their hobby is {final_contacts_list[]}.'")
        if inpt_name != dictionary['name']: #PROBLEM runs too many times
            print("That user cannot be found in this contact list.")
    return inpt_name

def update_contact(inpt_name):
        user_input_fh = input(f"Would you like to update {inpt_name}'s food or hobby? : ")

        if user_input_fh == 'food':
            inpt_food = input(f"What is {inpt_name}'s new favorite food? : ") #not sure if I can use user_input8 twice on two lines
            for dictionary in final_contacts_list:
                if dictionary['name'] == inpt_name:
                    dictionary['food'] = inpt_food

        if user_input_fh == 'hobby':
            inpt_hobby = input(f"What is {inpt_name}'s new hobby? : ")
            for dictionary in final_contacts_list:
                if dictionary['name'] == inpt_name:
                    dictionary['hobby'] = inpt_hobby
        else:
            print("That is not an option")
        return inpt_name

def delete_contact(inpt_name):
    for i in range(len(final_contacts_list)):
        if final_contacts_list[i]['name'] == inpt_name:
            del final_contacts_list[i]
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