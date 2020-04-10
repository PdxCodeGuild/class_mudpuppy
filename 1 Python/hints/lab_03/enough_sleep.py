user_sleep = input("How much did you sleep? ")
user_sleep = int(user_sleep)
if user_sleep < 5:
	print('Sleep more!')
if user_sleep > 10:
	print("That's too much")
if user_sleep >= 5 and user_sleep <= 10:
	print("Nice!")
