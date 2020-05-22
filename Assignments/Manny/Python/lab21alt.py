import string
import os
print(os.path.abspath(__file__))
BASE = os.path.dirname(os.path.abspath(__file__))
print(BASE + '/' + 'seneca.txt')
print(os.path.join(BASE, 'seneca.txt'))
with open(os.path.join(BASE, 'seneca.txt'), 'r') as f:
    bkstr = f.readlines():
for punc in string.punctuation:
    line = line.replace(punc, '')
    print(line.strip().split())
