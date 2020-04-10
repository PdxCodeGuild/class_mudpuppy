# scarf_gen.py
'''
The purpose of this program: create a series of patterns in the terminal, similar to randomly generating a patterned scarf.
'''
import random
pattern_list = ['##', '\\\\', '//', '~~', '**'] # a list of random patterns to choose from. Why four backslashes?
length = 10 # The vertical length of the pattern
out_string = '' # We start with our nucleus, a string with a length of zero.
for iteration in range(length):
    out_string += random.choice(pattern_list) * 5 # each time this runs, we add a random pattern from the list * 5
    out_string += '\n' # each time this runs, we add a newline to the string
print(out_string)
