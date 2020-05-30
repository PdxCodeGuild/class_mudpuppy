def rot13(phrase):
    abc = "abcdefghijklmnopqrstuvwxyz"
    abc2 = "nopqrstuvwxyzabcdefghijkl"
    out_phrase = "" #encrypted string originally empty
    for chr in phrase: #we want to encrypt each character in the phrase
        out_phrase += abc[(abc.find(chr)+13)%26] #we wound find the position at
    return out_phrase
phrase = input("input a phrase or letter: ")
encrypt = print(rot13(phrase))
decrpt = print(rot13(rot13(phrase)))