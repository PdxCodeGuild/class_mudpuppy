import os
import csv

BASE = os.path.dirname(os.path.abspath(__file__))
csv_file = "contacts.csv"


contacts = []


def get_contacts(CSV):
    with open(os.path.join(BASE, CSV), "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        for line in reader:
            contacts.append(line)       # TODO: change all keys to title case
    return contacts, header


def print_contact(contact):
    print()
    print(contact["name"] + "'s favorite food is " + contact["food"] + " and they enjoy " + contact["hobby"])


contacts, header = get_contacts(csv_file)


def create_contact():
    print("Please enter each field.")
    contact = {}
    for head in header:
        val = input(f"Please enter {head} ")
        contact[head] = val
    contacts.append(contact)
    return contacts


def seach_contacts():
    search_type = input("Search for name, food, or hobby? ").lower()
    if search_type not in header:
        print("Not a valid key.")
    else:
        query = input(f"Enter the {search_type}: ")
        for person in contacts:
            if person[search_type] == query:
                print_contact(person)


def update_contact():
    target = input("Enter a name to update: ").title()
    for contact in contacts:
        if contact["name"] == target:
            update_key = input("What would you like to update, ")
            update_value = input(f"Enter new {update_key} ")
            contact[update_key] = update_value
        else:
            print(f"{target} not in contacts.")
    return contacts


def delete_contact():
    target = input("Who would you like to delete? ").title()
    for contact in contacts:
        if contact["name"] == target:
            contacts.remove(contact)
            print(f"Removed {target}")
            break
        else:
            print(f"{target} not in contacts.")
    return contacts


def save_contacts(contacts, header):
    with open('friends.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for person in contacts:
            writer.writerow(person)
    print("The file was saved as friends.csv")



while True:
    try:
        print("\n\
==========MENU=========\n\
[1] CREATE   [2] DELETE\n\
[3] UPDATE   [4] SEARCH\n\
[5] SAVE     [0] QUIT")
        user_action = int(input(": "))
        if user_action == 1:
            create_contact()
        elif user_action == 4:
            seach_contacts()
        elif user_action == 3:
            update_contact()
        elif user_action == 2:
            delete_contact()
        elif user_action == 5:
            save_contacts(contacts, header)
        elif user_action == 0:
            break
        else:
            print("Enter a number 0 - 4")
    except KeyboardInterrupt:
        print("\nGoodbye")
        break
    except ValueError:
        print("\nNot a valid choice.  Please enter 0 - 4")
        continue
