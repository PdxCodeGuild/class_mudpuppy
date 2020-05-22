import math 

with open('ari.csv', 'r') as file:
    string = file.read()
    print(string) 

# string = 'And I am alone a good deal just now John is kept in town very often by serious cases, and Jennie is good and lets me alone when I want her to. So I walk a little in the garden or down that lovely lane, sit on the porch under the roses, and lie down up here a good deal. I\'m getting really fond of the room in spite of the wallpaper. Perhaps because of the wallpaper. It dwells in my mind so!'
 
n_sentences = 0
for char in string:
    if char in ['.','!','?']:
        n_sentences += 1
# print(n_sentences)
 
words = string.split()
n_words = len(words)
# print(n_words)
            
# print(words)

n_characters = 0
for word in words:
    n_characters += len(word)
# print(n_characters)


 
 
ari = (4.17 * (n_characters/n_words)) + ((n_words/n_sentences) * 0.5) - 21.43
 
if ari > 14:
    ari = 14

# print(ari)
# print(round(ari))
 
# The score is computed by multiplying the number of characters divided by the number of words by 4.17, adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. If the result is a decimal, always round up. Scores greater than 14 should be presented as having the same age and grade level as scores of 14.
 
 
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



grade_level = ari_scale[(round(ari))]


# print(grade_level)
 

print('Grade Level: ' + grade_level['grade_level']) 
print('Age: ' + grade_level['ages'])


