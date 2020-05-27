import string
import os
print(os.path.abspath(__file__))
BASE = os.path.dirname(os.path.abspath(__file__))
print(BASE + '/' + 'seneca.txt')
print(os.path.join(BASE, 'seneca.txt'))
with open(os.path.join(BASE, 'seneca.txt'), 'r') as f:
    bkstr = f.read() #reading seneca.txt 
bkstr = bkstr.lower()
 # called .lower function 

for punc in string.punctuation: # for loop looping and looking for punctuation n large book string
    bkstr = bkstr.replace(punc, '') # replace is replacing punctuation with empty string 
bklst = bkstr.split() # .split is a string method converts our string into a list 
seneca_word = {} # empty dictionary to added our word count soon
for word in bklst: # word is looking for for in bklist and looping over 
    if word in seneca_word.keys(): # if word is in dict then line 19 will run 
        seneca_word[word] = seneca_word[word] + 1 # when this line is ran it will add to the value linked the key 
    else:
        seneca_word[word] = 1 # creates new key value pairing "{word: number}"

def get_index_one(intup):# returning index 1 from tuples in dict
    return intup[1]


final_bk = list(seneca_word.items())

final_bk.sort(key=get_index_one, reverse=True) #revers=True largest to smallest reverse = False smallest to largest
print(f"{final_bk[0:10]}") #final_bk[0:10] lets us how much of the returned sorted indices we would like.