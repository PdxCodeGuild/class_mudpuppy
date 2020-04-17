#lab19-blackjack-advice.py

def card_value(user_input):
    if user_input in '2, 3, 4, 5, 6, 7, 8, 9, 10'.split(', '):
        user_input = int(user_input)
    elif user_input in 'jqk':
        user_input = 10
    else:   
        user_input = 1   

    return user_input

#start at 0
total_value = 0 

for index in range(3):
    user_input = (input('What is your card?'))
#adding to total value
    total_value += (card_value(user_input ))
print(total_value)

if total_value < 17:
    print('hit')
elif total_value >= 17 and total_value < 21:
    print ('stay')
elif total_value == 21:
    print('Blackjack!')
else:
    print ('Already Busted!')
