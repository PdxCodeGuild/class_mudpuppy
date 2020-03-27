import random

eye = random.choice(';:')
nose = random.choice('->')
mouth = random.choice(')]')
output = eye + nose + mouth
print(output)

def make_face(eye, nose, mouth):
    return eye + nose + mouth

# def make_eye():
#     return 

# def make_nose():
#     return 

# def make_mouth():
#     return 

#print(make_face(make_eye(), make_nose(), make_mouth()))
#print(make_face(';', '>', ']'))

