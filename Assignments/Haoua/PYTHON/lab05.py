import random

eyes = ["B", ":", ";",]
noses = ["-","^","o", "7" ]
mouth = [")", "]","D","p", "b", "*", "/", "0"]
person = random.choice(eyes) + random.choice(noses) + random.choice(mouth)
print(person)

i = 0
while i < 4:
    print(random.choice(eyes) + random.choice(noses) + random.choice(mouth))
    i += 1
    
    