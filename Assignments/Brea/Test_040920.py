#Test Examples April 9th, 2020

# data = [('Brea', 'Ice Cream'),('Pete', 'Gnocchi'),('Terrance','Pizza'), ('Manny', 'Chili Cheese Fries'), ('Kadir', 'Lasagna'), ('Al', 'Burrito')]

# for var1, var2 in data:     #unpacking the tuples when var1, var2 pointed at in for loop
#     print(var2)

#------------------------------------
#emotion_tracker.py
# '''
# happy_counter = 0
# while True:
#     user_input = ("How are you feeling? : ")
#     if user_input == 'happy':
#         counter += 1
#     elif user_input == 'done':
#         break
# print(happy_counter)
# '''

emotion_counter = {}
while True:
    user_input = ("How are you feeling? : ")
    if user_input == 'done':
        break
    if user_input in emotion_counter.keys():
        emotion_counter[user_input] = emotion_counter[user_input] + 1
    else:
        emotion_counter[user_input] = 1

# print emotion_counter

# emotion_counter.items()
# for one_tup in emotion_counter.items(): #for each of the tuples as listed within the items function
#     print(one_tup[1]) #prints out just values (i.e., number counts) within dictionary from emotion_counter dict

def return_index_one(in_tup):   #function that gives me the number counter within tuples created by emtoin_counter.items()
    return in_tup[1]

tup_list = list(emotion_counter.items())
print(tup_list)
tup_list.sort(key=return_index_one, reverse=True) #returns list of the tuples that sorts them by which has the highest counter (i.e., index one of the tuple) per our return_index_one function above

# print(f"You mostly feel {emotion_counts[0][0]}")


how to open a file, list_of_words.py
with f as open
with open('test_words.txt') as f:
    for line in f.readlines():
        for punc in string.punctuation:
            line = line.replace(punc, '')
        print(line.strip().split())
        # print(line.strip().split()) #creates two lists, one per line with one word as an item in the list

#--------------------------------------------

import os
print(os.path.abspath(__file__)) #tells me where my file is
print(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.dirname(os.path.abspath(__file__))
print(BASE)
print(os.path.join(BASE, 'words.txt')) #created a new path with words.txt in it, always does the "right" thing based on your operating system

with open(os.path.join(BASE, 'words.txt')) #right next to this file, there should be something called txt