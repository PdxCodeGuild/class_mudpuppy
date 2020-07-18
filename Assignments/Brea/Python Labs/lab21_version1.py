#Lab 21, version 1, April 9th, 2020
import string

word_dict = {}

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
        for word in line:
            if word in word_dict.keys():
                word_dict[word] = word_dict[word] + 1
            else:
                word_dict[word] = 1
    print(word_dict)

def sort_by_index_one(tup):
    return tup[0]


words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=sort_by_index_one, reverse=True) #another way to run line 31
# words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
print(words[:10])