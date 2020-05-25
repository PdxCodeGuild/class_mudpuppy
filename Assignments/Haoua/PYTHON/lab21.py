import string

punct=string.punctuation


f= open("PYTHON/text.txt","r",  encoding="utf-8")


list1 = []

for line in f.readlines():
    for punc in punct:
        line = line.replace(punc,"")
        lines = line.strip("\ufeff")
        lines12=lines.strip()
        strip_list = lines12.split()
    list1.append(lines12.lower().split())
print(list1)


dict1 = dict()
for word in list1:
    for i in word:
        
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
print(dict1)

#-----------------------------------------
'''top 10 frequent (highest to lowest)'''
words_list = list(dict1.items()) 
sorted_list= words_list.sort(key=lambda tup: tup[1], reverse=True)  

for pairs in range((10)):
    print(words_list[pairs])
#----------------------------------------
'''version 2(top 10 unique (lowest)''' 
words_list = list(dict1.items()) 
unique_list = words_list.sort(key=lambda tup: tup[1]) 
for upairs in range((10)):
     print(words_list[upairs])

