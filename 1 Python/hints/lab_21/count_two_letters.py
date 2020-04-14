#count_double_letters.py

input_string = 'sntthueoasntthueeoasnthaoueoaeooa'

double_letter_counter = {}
for index in range(len(input_string) - 1):
    active_letter = input_string[index]
    next_letter = input_string[index + 1]
    letter_tup = (active_letter, next_letter) 
    if letter_tup in double_letter_counter:
        double_letter_counter[letter_tup] += 1
    else:
        double_letter_counter[letter_tup] = 1

print(double_letter_counter)
'''
 if user_input in emotion_counter.keys(): # we've seen the word before
        emotion_counter[user_input] = emotion_counter[user_input] + 1
    else:
        emotion_counter[user_input] = 1 # we just 
'''