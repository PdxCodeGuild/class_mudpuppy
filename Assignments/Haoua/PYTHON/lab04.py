import random

print("Welcome to the Magic 8 Ball!")

predictions1 = ["Maybe", "Without a doubt", "It is certain", "Outlook good"]
predictions2 = ["Ask again later", "Better not tell you know", "Bitch idk", "Only God can knows the answer", "Ask the Dalai Lama", "Do you ask your friends these questions?", "How tf am I supposed to know?"]
predictions3 = ["Dount count on it", "In your dreams", "My reply is FUCK NO", "My sources say nah", "I feel sorry for you"]

user = input("Ask me a question : ")

final = predictions1 + predictions2 + predictions3
final2 = print(random.choice(final))

user2 = input("Would you like to ask another question? : ")
user3 = user2.lower()

response = ["yes", "yeh", "y", "yeah", "sure", "ok"]
# response2 = ["no", "nah", "n", "negative", "im good", "i'm good", "nay", "nope"]

while True:
    if user3 in response:
        input("Ask me a question : ")
        print(random.choice(final))
        user3 = input("Would you like to ask another question? : ")   
        continue
            # if user4 in response:
            #     print("Ask me a question") # break
            # else:
            #     print(Thank you for playing)
    else:
        print("Thank you for playing")
        break
