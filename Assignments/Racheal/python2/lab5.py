import random

eyes = [";",":","="]
nose = ["^","o","-",]
mouth =["O",")","(","p","b","*","D"]

person = random.choice(eyes) + random.choice(nose) + random.choice(mouth)
print(person)



x = 0

while x < 4:

    print(random.choice(eyes) + random.choice(nose) + random.choice(mouth))

    x += 1