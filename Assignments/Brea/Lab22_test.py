import string

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

char_num = 0
words_num = 0
sent_num = 0

def readability(char_num, words_num, sent_num):
    ari_score = round((4.71 * (char_num / words_num)) + (0.5 * (words_num / sent_num)) - 21.43)
    return ari_score

import os
print(os.path.abspath(__file__)) 
BASE_dir = (os.path.dirname(os.path.abspath(__file__)))
text_file = os.path.join(BASE_dir, 'beautiful_and_damned.txt')

with open(text_file) as f:
    for baseline in f.readlines():
        line = baseline.strip().split()
        for word in line:
            if '.' in word:
                sent_num += 1
    
        line = baseline
        for punc in string.punctuation:
            line = line.replace(punc, '')
        line = line.strip().split()

        words_num += len(line)

        for punc in string.punctuation:
            line = baseline.replace(punc, '')
        for index in line:
            line = line.replace(' ', '')
        for char in line:
            char_num +=1

print(f"There are {char_num} characters, {words_num} words, and {sent_num} sentences.")

ari_score = readability(char_num, words_num, sent_num)

print(f"The ARI for your text file is {ari_score}. This corresponds to a {ari_scale[ari_score]['grade_level']} level of difficulty and is suitable for your typical {ari_scale[ari_score]['ages']} year old")