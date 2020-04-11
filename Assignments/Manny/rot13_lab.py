rot_alpha = { #created a dictionary to call encoded message
    'a' : 'n', 'A' : 'N',
    'b' : 'o', 'B' : 'O',
    'c' : 'p', 'C' : 'P',
    'd' : 'q', 'D' : 'Q',
    'e' : 'r', 'E' : 'R',
    'f' : 's', 'F' : 'S',
    'g' : 't', 'G' : 'T',
    'h' : 'u', 'H' : 'U',
    'i' : 'v', 'I' : 'V', 
    'j' : 'w', 'J' : 'W',
    'k' : 'x', 'K' : 'X',
    'l' : 'y', 'L' : 'Y',
    'm' : 'z', 'M' : 'Z',
    'n' : 'a', 'N' : 'A',
    'o' : 'b', 'O' : 'B',
    'p' : 'c', 'P' : 'C',
    'q' : 'd', 'Q' : 'D',
    'r' : 'e', 'R' : 'E',
    's' : 'f', 'S' : 'F',
    't' : 'g', 'T' : 'G',
    'u' : 'h', 'U' : 'H',
    'v' : 'i', 'V' : 'I',
    'w' : 'j', 'W' : 'J',
    'x' : 'k', 'X' : 'K',
    'y' : 'l', 'Y' : 'L',
    'z' : 'm', 'Z' : 'M'
    }

coded = ""
uncoded = input("Please type in the message you would like to encode: ") # asking user for thier message they would like to code
for letter in uncoded:
    if letter in rot_alpha:
        coded = coded + rot_alpha[letter]
    else:
        coded = coded + letter     
print(coded)
    