import string

f= open("PYTHON/text.txt","r",  encoding="utf-8")
punct = string.punctuation

sentences = 0
list1 = []
'''
for line in f.readlines():
    for punc in punct:
        line = line.replace(punc,"")
        lines = line.strip("\ufeff")
        lines12=lines.strip()
        strip_list = lines12.split()
    list1.append(lines12.lower().split())
print(list1)
'''
indicators = ".!?"
      
# with open('contacts.csv', 'r') as file:
#     lines = file.rea  line = line.replace(punc,"")"d().strip().split('\n')
list2=[]
for lines in f.readlines():
    line=lines.strip("\ufeff")
    newline=line.strip()
    newlines=newline.split()
    chars=(len(newlines))
    list1.append(chars)
    # print(newlines)
    
    # for i in lines:
    for i in lines:
    # print(i)
        if i in punct:
            
        

            special= newline.replace(i,"")
            list2.append(special.split())
        if i in indicators:
            sentences +=1
        else:
            pass

        # print(new)
    # print(newline)



characters=sum(list1)
words = len(list2)

print(sentences)
print(words)
print(characters)

print(f'Your Ari is: {int((4.71*(characters/words)) +(0.5*(words/sentences))-21.43)}')
ari= int(input("retype your ari here: "))







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
def myfunc(ari):
    if ari < 14:
        grade= (ari_scale[ari]["grade_level"])
        age= (ari_scale[ari]["ages"])
    else:

        grade = (ari_scale[14]["grade_level"])
        age = (ari_scale[14]["ages"])

    if ari//14 == 1/14:
        print(f"The ARI for this Text is {ari} This corresponds to a {ari1} level of difficulty that is suitable for an average person  years old.")

    elif ari/14 == 2/14:
        print(f"The ARI for this Text is {ari} This corresponds to a {grade} level of difficulty that is suitable for an average person {age} years old.")
    elif ari/14 == 3/14:
        print(f"The ARI for this Text is {ari} This corresponds to a {grade} level of difficulty that is suitable for an average person {age} years old.")
    elif ari/14 == 4/14:
        print(f"The ARI for this Text is {ari} This corresponds to a {grade} level of difficulty that is suitable for an average person {age} years old.")
    elif ari/14 == 5/14:
        print(f"The ARI for this Text is {ari} This corresponds to a {grade} level of difficulty that is suitable for an average person {age} years old.")
    elif ari/14 == 6/14:
        print(f"The ARI for this Text is {ari} This corresponds to a {grade} level of difficulty that is suitable for an average person {age} years old.")
    elif ari/14 == 7/14:
        print(f"The ARI for this Text is {ari} This corresponds to a {grade} level of difficulty that is suitable for an average person {age} years old.")
    elif ari/14 == 8/14:
        print(f"The ARI for this Text is {ari} This corresponds to a {(grade)} level of difficulty that is suitable for an average person {age} years old.")
    elif ari/14 == 9/14:
        print(f"The ARI for this Text is {ari} This corresponds to a {grade} level of difficulty that is suitable for an average person {age} years old.")
    elif ari/14 == 10/14:
        print(f"The ARI for this Text is {ari} This corresponds to a {(grade)} level of difficulty that is suitable for an average person {age} years old.")

    elif ari/14 == 11/14:
        print(f"The ARI for this Text is {ari} This corresponds to a {grade} level of difficulty that is suitable for an average person {age} years old.")

    elif ari/14 == 12/14:
        print(f"The ARI for this Text is {ari} This corresponds to a {grade} level of difficulty that is suitable for an average person {age} years old.")

    elif ari/14 == 13/14:
        print(f"The ARI for this Text is {ari} This corresponds to a {grade} level of difficulty that is suitable for an average person {age} years old.")

    elif ari/14 >= 1:
        print(f"The ARI for this Text is {ari} This corresponds to a {grade} level of difficulty that is suitable for an average person {age} years old.")

    else:
        print("it's broken")

myfunc(ari)




