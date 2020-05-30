
import string


text = ( "A a a SIMULTANEOUS effort is this day being made in this parish by ministers of various sections of the one church of christ to direct public attention to a question of no ordinary magnitude, with which the cause of national righteousness is identified; and to stir up the community tounite in vigorous, yet peaceful opposition to a project, which involves the perpetration of a great national sin." )
 
 

lowercase = text.lower()

punctuation = '!#$%&()*+,-./:;?@[\]^_`{|}~"'

for punc in punctuation:
    lowercase = lowercase.replace(punc, '')

words_list = lowercase.split()


word_dict = {}




for word in words_list:
            if word in word_dict.keys():
                word_dict[word] = word_dict[word] + 1 # add and count 
            else:
                word_dict[word] = 1 


print(word_dict)



words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])





# print(word_dict)