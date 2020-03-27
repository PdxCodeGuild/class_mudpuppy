def average(x,y):
    return (x + y) // 2

def search(lower, upper, target, guess):
    print(f'You guessed {guess}')

    if guess == target:
        print('Correct')
    elif guess < target:
        print('Too low.')
        search(guess, upper, target, average(guess, upper)+1)
    elif guess > target:
        print('Too high.')
        search(lower, guess, target, average(lower, guess))


search(1,100,1,2)
