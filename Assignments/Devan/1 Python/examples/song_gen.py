import random
note_list = ['doo', 'da', 'day']
# print(random.choice(note_list) + random.choice(note_list))
note_num = input("How many notes? ")
note_num = int(note_num)
out_song = ''
for i in range(note_num):
    out_song = out_song + random.choice(note_list)
print(out_song)
