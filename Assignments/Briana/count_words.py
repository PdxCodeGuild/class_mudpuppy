# still need to import file and go over lambda tup: tup[1] video 

import string


text = ( "It is very seldom that mere ordinary people like John and myself secure ancestral halls for the summer. A colonial mansion, a hereditary estate, I would say a haunted house, and reach the height of romantic felicity but that would be asking too much of fate! Still I will proudly declare that there is something queer about it. Else, why should it be let so cheaply? And why have stood so long untenanted? John laughs at me, of course, but one expects that in marriage. John is practical in the extreme. He has no patience with faith, an intense horror of superstition, and he scoffs openly at any talk of things not to be felt and seen and put down in figures. John is a physician, and perhaps (I would not say it to a living soul, of course, but this is dead paper and a great relief to my mind) perhaps that is one reason I do not get well faster. You see, he does not believe I am sick! And what can one do?" )
 
 

lowercase = text.lower()

punctuation = '!#$%&\'()*+,-./:;?@[\]^_`{|}~\"'

for punc in punctuation:
    lowercase = lowercase.replace(punc, '')

words_list = lowercase.split()


word_dict = {}




for word in words_list:
            if word in word_dict.keys():
                word_dict[word] = word_dict[word] + 1 # add and count it
            else:
                word_dict[word] = 1 # leave it at the same number, don't add for word in text:


print(word_dict)



words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])





# print(word_dict)

