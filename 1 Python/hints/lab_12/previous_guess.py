# previous_guess.py
first_run = True # It is the first run of the loop
while True: # REPL until the user types 'done'
    user_guess = input("Type a number >")
    if user_guess == 'done':
        break
    if first_run == True: # If it is the first run of the loop
        print(f"You guessed {user_guess}") # It's the first run, don't print previous guess
        old_guess = user_guess
        first_run = False # We're finishing the first run, so we'll set first_run to False
    else: # If it's not the first run of the loop
        print(f"You guessed {old_guess} and then {user_guess}") # It's not the first run, so print old and new
        old_guess = user_guess
