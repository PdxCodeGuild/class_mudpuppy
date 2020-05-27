import random 
print("Welcome to the Magic 8 Ball!")

predictions1 = ["Don't count on it", "Easily", "It is certain", "It's lookin really good", "NAW"]
predictions2 = ["Try again later", "Better not tell you know", "IDK", "Who even knows", "Ask Jesus"]
predictions3 = ["Reply hazy", "In your dreams", "Duh", "My reply is no.", "YAS"]

user = input("Ask the Magic 8 Ball a question : ")

final = predictions1 + predictions2 + predictions3
final2 = print(random.choice(final))

user2 = input("Want to keep going? : ")
user3 = user2.lower()

response = ["yes", "yeah", "yas", "please"]

while True:
    if user3 in response:
        input("Ask me a question : ")
        print(random.choice(final))
        user3 = input("Would you like to ask another question? : ")
        continue
    else:
        print("Thank you for playing")
        break