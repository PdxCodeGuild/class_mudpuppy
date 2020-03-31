# enough_sleep.py

user_sleep = int(input("How much did you sleep last night? "))
if user_sleep < 5:
    print("Sleep more!")
if user_sleep > 10:
    print("Get up lazy!")
if user_sleep >= 5 and user_sleep <= 10:
    print("Good job!")