

lower = 0
upper = 100

def average(x,y):
    return (x + y) // 2

def search(lower, upper, value, guess, num_tries):
    print(f'You guessed {guess}')
    if guess == value:
        print(f'You got it in {num_tries} tries')
    elif guess < value:
        print('Too low')
        return search(guess, upper, value, average(guess, upper), num_tries+1)
    elif guess > value:
        print('Too high')
        return search(lower, guess, value, average(guess, lower), num_tries+1)

search(0,100, 34, 1, 0)