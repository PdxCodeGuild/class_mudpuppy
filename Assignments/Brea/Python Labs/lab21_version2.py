#Lab 21, version 2, April 9th, 2020
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

        for index in range(len(line) - 1):
            word1 = line[index]
            word2 = line[index+1]
            words = line[index] + ' ' + line[index+1]
            print(words)
            if words in word_dict.keys():
                word_dict[words] = word_dict[words] + 1
            else:
                word_dict[words] = 1
    print(word_dict)

words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])