print("You are running or importing contacts.py!")

class Contact:
    def __init__(self, name_param, food_param, game_param):
        self.name_attr = name_param
        self.food_attr = food_param
        self.game_attr = game_param

    @staticmethod
    def find_contact(search_name):
        with open('contact.csv', 'r') as f:
            for line in f.readlines():
                line = line.split(',')
                if search_name.lower() == line[0].lower():
                    return Contact(
                        name_param = line[0],
                        food_param = line[1],
                        game_param = line[2],
                    )

if __name__ == "__main__":
    found_contact = Contact.find_contact('Al')
    print(found_contact.name_attr, found_contact.food_attr, found_contact.game_attr)