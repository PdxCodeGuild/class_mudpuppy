# lab2
"""
instructions
Search the interwebs for an example Mad Lib
Create a new file and save it as madlib.py
Ask the user for each word you'll put in your Mad Lib
Use an fstring to put each word into the Mad Lib
"""
"""
The wheels on the bus go round and round
Round and round
Round and round
The wheels on the bus go round and round
All through the town
"""
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
# There was a farmer who had {noun},
# And Bingo was his name-o.
# B-I-N-G-O
# And Bingo was his name-o.
# There was a farmer who had a dog,
# And Bingo was his name-o.
print(f"There was a farmer who {verb}, {adjective},And {noun} was his name-o.")