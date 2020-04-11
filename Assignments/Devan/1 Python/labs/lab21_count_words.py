import os
import string
from huepy import *

BASE = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(BASE, 'TheCalloftheWild.txt')) as book:
    contents = book.read()


def lower_and_split(contents):
    """ Looks at each character of contents and removes punctuation then returns a list of all words. """
    results = ''
    contents = contents.lower()
    for char in contents:
        if char not in string.punctuation:
            results += char
    results = results.split()
    return results


def count_words(contents):
    """ Creates a word_counts dictionary containing each word and how many times it was used. """
    results = lower_and_split(contents)
    word_counts = {}
    for word in results:
        if word not in word_counts:
            word_counts[word] = 1
        word_counts[word] += 1
    return word_counts


def top_10(word_counts):
    """ Sorts the word_count dictionary and prints the top 10 used words and their counts. """
    words = list(word_counts.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print('The word ' + bold(blue(words[i][0])) + ' was mentioned ' + bold(blue(words[i][1])) + ' times.')


top_10(count_words(contents))
