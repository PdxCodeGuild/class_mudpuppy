import os
import string

BASE = os.path.dirname(os.path.abspath(__file__))
BOOK = "TheGettysburgAddress.txt"

with open(os.path.join(BASE, BOOK)) as book:
    text = book.read().lower()



def calc_ari(chars, words, sentences):
    ari = round(4.71*(chars/words)+0.5*(words/sentences)-21.43)
    if ari > 14:
        ari = 14
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
    print("-------------------------------------------------")
    print(f"The ARI for {BOOK} is {ari}.")
    print(f"This corresponds to a {ari_scale[ari]['grade_level']} level \nthat is suited for ages {ari_scale[ari]['ages']} years old. ")
    print("-------------------------------------------------")


def count_characters(text):
    count = 0
    for char in text:
        if char in string.ascii_letters:
            count +=1
    print(f'Chars: {count}')
    return count


def count_words(text):
    results = ''
    for char in text:
        if char not in string.punctuation:
            results += char
    results = results.split()
    word_count = len(results)
    print(f'Words: {word_count}')
    return word_count


def count_sentences(text):
    sentence_count = 0
    for char in text:
        if char in ".!?":
            sentence_count += 1
    print(f'Sentences: {sentence_count}')
    return sentence_count


# def count_sentences(text):
#     sentence_count = text.count('.')
#     return sentence_count



# count_words(text)
# count_characters(text)
# count_sentences(text)
calc_ari(count_characters(text), count_words(text), count_sentences(text))
