# good_day.py

days = {}
while True:
    user_name = input("What is your name? ")
    user_day = input("Did you have a good day? ('q' to quit) ")
    if 'yes' == user_day:
        print("Woohoo!")
        days[user_name] = user_day
    if 'no' == user_day:
        print("Too bad")
        days[user_name] = user_day
    if user_day == 'q':
        break
print(days)




