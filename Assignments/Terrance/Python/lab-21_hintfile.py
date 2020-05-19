#lab-21_hintfile.py

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
    user_input = input("How are you feeling? ") # user inserts emotion
    if user_input == "done": # breaks the
        break
    if user_input in emotion_counter.keys(): # we've seen the word before
        emotion_counter[user_input] = emotion_counter[user_input] + 1
    else:
        emotion_counter[user_input] = 1 # we just heard it once
print(emotion_counter)

emotion_counts = list(emotion_counter.items()) # makes a list
def return_index_one(in_tup):
    return in_tup[1]
emotion_counts.sort(key=return_index_one, reverse=True) # sorting by count
print(f"You mostly feel {emotion_counts[0][0]}")


# Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal. Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

# Find a book on Project Gutenberg. Download it as a UTF-8 text file.

#     Open the file.
#     Make everything lowercase, strip punctuation, split into a list of words.
#     Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
#     Print the most frequent top 10 out with their counts. You can do that with the code below.
