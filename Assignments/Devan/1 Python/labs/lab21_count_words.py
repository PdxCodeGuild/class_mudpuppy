import os
import string
from huepy import *


BASE = os.path.dirname(os.path.abspath(__file__))


word_counter = {}

with open(os.path.join(BASE, 'TheCalloftheWild.txt')) as book:
    for line in book.readlines():
        for punc in string.punctuation:
            line = line.replace(punc, '').lower().strip()
        for word in line.split():
            if word in word_counter.keys():
                word_counter[word] += 1
            else:
                word_counter[word] = 1

words = list(word_counter.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print('The word ' + bold(blue(words[i][0])) + ' was mentioned ' + bold(blue(words[i][1])) + ' times.')
