import string
words = 0
characters = 0
lines = 0
with open("robertfrost2.txt", 'r') as f:
    for line in f.readlines():
        line = line.lower()
        for punc in string.punctuation:
            line = line.replace(punc, '')
        characters = characters + len(line.strip().replace(' ', ''))
        line_list = line.split()
        words = words + len(line_list)
        if lines in line_list:
          line_list[lines] = lines_list[lines] isn't just new line:
        else: 
            lines +=1
    print(words,characters,lines)
