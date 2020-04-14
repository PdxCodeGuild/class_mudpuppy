import os
import string

BASE = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(BASE, 'TheCalloftheWild.txt')) as book:
    text = book.read().lower()


def calc_ari(character_count, word_count, sentence_count):
    text_ari = round(4.71*(character_count/word_count)+0.5*(word_count/sentence_count)-21.43)
    print(text_ari)


def count_characters(text):
    results = ''
    for char in text:
        if char not in string.punctuation:
            if char not in string.whitespace:
                results += char
    character_count = len(results)
    return character_count


def count_words(text):
    results = ''
    for char in text:
        if char not in string.punctuation:
            results += char
    results = results.split()
    word_count = len(results)
    return word_count


def count_sentences(text):
    sentence_count = text.count('.')
    return sentence_count



# count_words(text)
# count_characters(text)
# count_sentences(text)
calc_ari(count_characters(text), count_words(text), count_sentences(text))
