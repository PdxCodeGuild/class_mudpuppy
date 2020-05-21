#Lab 21, version 3, April 13th, 2020

import string

word_search_dict = {}

user_input = input("What word would you like to search for? : ")

import os
print(os.path.abspath(__file__)) #tells me where my file is
BASE_dir = (os.path.dirname(os.path.abspath(__file__)))
text_file = os.path.join(BASE_dir, 'the_time_machine.txt')
print(text_file)

with open(text_file) as f:
    for line in f.readlines():
        line = line.lower()
        for punc in string.punctuation:
            line = line.replace(punc, '')
        line = line.strip().split()
    
        for index in range(len(line) -  1):
            search_word = line[index]
            follow_word = line[index + 1]
            word_tup = (search_word, follow_word)
        
            if search_word == user_input:
                if word_tup in word_search_dict:
                    word_search_dict[word_tup] += 1
                else:
                    word_search_dict[word_tup] = 1
    
words_list = list(word_search_dict.items())
words_list.sort(key=lambda tup: tup[1], reverse=True) #returns a list of tuples
#user_words = [word for word in words_list if user_input == word] #same as line 37 for loop


user_words = []
for word in words_list:
    if user_input == word[0][0]:
        user_words.append(word)

for i in range(min(5, len(user_words))): #sorts largest to smallest by count
    print(user_words[i])

word1 = user_words[0][0][1]
word2 = user_words[1][0][1]
word3 = user_words[2][0][1]
word4 = user_words[3][0][1]
word5 = user_words[4][0][1]

print(f"The top 5 words that follow {user_input} in this text are 1. {word1}, 2. {word2}, 3. {word3}, 4. {word4}, and 5. {word5}")