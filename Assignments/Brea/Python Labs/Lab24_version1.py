#Lab 24, Version 1, April 20th, 2020

#print(contents[1:527])

with open('opb.rain.txt', 'r') as f:
    #contents = f.read()
    for line in f.readlines()[:20]:
        print(line)

#regex to grab date column = \d\d-\w{3}-\d{4}