# emotion_tracker.py
'''
happy_counter = 0
while True:
    user_input = input("How are you feeling? ")
    if user_input =="happy":
        happy_counter = happy_counter + 1 # same as happy_counter += 1
    elif user_input == "done":
        break
print(happy_counter)
'''
emotion_counter = {}
while True:
    user_input = input("How are you feeling? ")
    if user_input == "done":
        break
    if user_input in emotion_counter.keys(): # we've seen the word before
        emotion_counter[user_input] = emotion_counter[user_input] + 1
    else:
        emotion_counter[user_input] = 1 # we just heard it once
print(emotion_counter)

emotion_counts = list(emotion_counter.items())
def return_index_one(in_tup):
    return in_tup[1]
emotion_counts.sort(key=return_index_one, reverse=True)
print(f"You mostly feel {emotion_counts[0][0]}")