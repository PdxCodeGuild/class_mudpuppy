import random

eyebrows = ['>' , '|' ]
eyes = [':' ,'8' , 'X']
noses = ['O' , 'U' , '@' , '*']
mouths = ['D' , 'O' , ')' , 'P']
eyebrows = random.choice(eyebrows)
eyes = random.choice(eyes)
noses = random.choice(noses)
mouths = random.choice(mouths)
emoticon = (f'{eyebrows} {eyes} {noses} {mouths}')
print(emoticon)

# Advanced Version 1
# Use a for loop to generate 5 emoticons.

# for x in range(5):
#     emoticon = random.choice(f'{eyebrows} {eyes} {noses} {mouths}')
#     print(emoticon)


# emoticon = ''
# i = 0
# while i >= 5 :
#     emoticon += random.choice(f'{eyebrows} {eyes} {noses} {mouths}')
#     i+=1
#     print(emoticon)




