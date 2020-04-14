import os
import string
from huepy import *

BASE = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(BASE, 'TheCalloftheWild.txt')) as book:
    contents = book.read()


def list_words(contents):
    """ Looks at each character of contents and removes punctuation then returns a list of all words. """
    results = ''
    contents = contents.lower()
    for char in contents:
        if char not in string.punctuation:
            results += char
    results = results.split()
    return results


def count_words(contents):
    """ Creates a dictionary containing each word and how many times it was used then prints the top ten. """
    results = list_words(contents)
    word_counts = {}
    for word in results:
        if word not in word_counts:
            word_counts[word] = 1
        word_counts[word] += 1
    print_top_ten(word_counts)
    return word_counts


def find_pairs(results):
    """ Finds all the pairs of words that occur, prints the top 10, and returns a dict. """
    unique_pairs = {}
    for word in range(len(results)-1):
        pair = str(results[word] + ' ' + results[word+1])
        if pair not in unique_pairs:
            unique_pairs[pair] = 1
        else:
            unique_pairs[pair] += 1
    print_top_ten(unique_pairs)
    return unique_pairs


def find_followers(contents):
    """ Finds all the words that follows the entered word then prints the top ten. """
    user_word = input("Enter a word: ")
    followers = {}
    for i in range(len(contents)-1):
        word_pair = (contents[i], contents[i+1])
        if word_pair[0] == user_word:
            if word_pair in followers:
                followers[word_pair] += 1
            else:
                followers[word_pair] = 1
    print_top_follwers(followers, user_word)
    return followers, user_word


def print_top_follwers(dict, user_word):
    """ Used in find_followers(), prints the top ten tuples. """
    dict = list(dict.items())
    dict.sort(key=lambda tup: tup[1], reverse=True)
    if len(dict) == 0:
        print('Did not find the word ' + bold(blue(user_word)))
        return
    for i in range(min(10, len(dict))):
        print('The pair ' + bold(blue(dict[i][0][0])) + ' ' + bold(blue(dict[i][0][1])) + ' was mentioned ' + bold(blue(dict[i][1])) + ' times.')


def print_top_ten(dict):
    """ Sorts the unique pairs of words and prints the top 10 used words and their counts. """
    pairs = list(dict.items())
    pairs.sort(key=lambda tup: tup[1], reverse=True)
    for i in range(min(10, len(pairs))):
        print('The pair ' + bold(blue(pairs[i][0])) + ' was mentioned ' + bold(blue(pairs[i][1])) + ' times.')


find_followers(list_words(contents))

# count_words(contents)
