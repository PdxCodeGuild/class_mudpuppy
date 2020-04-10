#lab13-rot_cypher.py

# Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.


English_ROT13dict = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':"z", 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m'}

message = 'Zrffntr zr lbhe svefg naq ynfg anzr, naq jung glcr bs jbex lbh ubcr gb qb jura lbh tenqhngr. Nyfb fraq zr n cnentencu funevat ubj lbh orpnzr vagrerfgrq va pbzchgre cebtenzzvat.'

output = ''
for eng in message:
    if eng.lower() in English_ROT13dict:
        output += (English_ROT13dict[eng.lower()])
    
    if eng in ' .,':
        output += (eng)
      
print(output)

