# list_of_words.py
'''
import string
with open("words.txt", 'r') as f:
    for line in f.readlines():
        for punc in string.punctuation:
            line = line.replace(punc, '')
        print(line.strip().split())
'''
import os
print(os.path.abspath(__file__))
BASE = os.path.dirname(os.path.abspath(__file__))
print(BASE + '/' + 'words.txt')
print(os.path.join(BASE, 'words.txt'))
with open(os.path.join(BASE, 'words.txt'))