#lab22-compute_automated_readability.py

import math

character_count = 0 
word_count = 0 # len(line.split())
sentence_count = 0 # line

with open("lab22-text.txt", 'r', encoding = "utf8") as f: # opening the file and naming the variable "f"
    for line in f.readlines(): # breaks the code into lines by \n

        word_count = word_count + len(line.split()) # splits the words and counts them 
        word_list = line.split() # splits the words in sentences
        
        for word in word_list:
            character_count = character_count + len(word) # splits the characters and counts them
            if word[-1] == "." or word == "!" or word == "?": # if the last character is a period, exclamation mark or question mark count it as a sentence
                sentence_count += 1

print(word_count, character_count, sentence_count)

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

ari = (4.71 * (character_count / word_count)) + (0.5 * (word_count / sentence_count)) - (21.43)

ari = math.ceil(ari)

print(ari_scale[math.ceil(ari)])

print(round(ari))

print(f"The ARI for your text file is {ari}. This corresponds to a {ari_scale[ari]['grade_level']} level of difficulty and is suitable for your typical {ari_scale[ari]['ages']} year old")