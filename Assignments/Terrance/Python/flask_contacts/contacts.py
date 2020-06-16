print("You are running or importing contacts.py!")

class Contact:
    def __init__(self, name_param, food_param, game_param):
        self.name_attr = name_param
        self.food_attr = food_param
        self.game_attr = game_param

    @staticmethod
    def find_contact(search_name):
        with open('contacts.csv', 'r') as f:
            for line in f.readlines():
                print (line)
                line = line.split(',')
                if search_name.lower() == line[1].lower():
                    return Contact(
                        name_param = line[1],
                        food_param = line[2], 
                        game_param = line[3],
                    )
    @staticmethod
    def find_by_id(search_id):
        with open('contacts.csv', 'r') as f:
            for line in f.readlines():
                line = line.split(',')
                if search_id == line[0]:
                    return Contact(
                        name_param = line[1],
                        food_param = line[2],
                        game_param = line[3],
                    )

if __name__ == "__main__":
    found_contact = Contact.find_contact('Al')
    print(found_contact.name_attr, found_contact.food_attr, found_contact.game_attr)