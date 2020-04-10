#military_letter_gen.py 

user_letters =  input('Give me some letters: ')
mil_dict = {'a' : 'alpha',
'b' : 'bravo',
'c' : 'charlie'}
output = ' ' 
for letter in user_letters:
    output += mil_dict[letter] + ' '

print(output)