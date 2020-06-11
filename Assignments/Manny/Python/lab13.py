rot13_dict = {
    'a':'n', 
    'b':'o', 
    'c':'p', 
    'd':'q', 
    'e':'r', 
    'f':'s', 
    'g':'t', 
    'h':'u', 
    'i':'v', 
    'j':'w', 
    'k':'x', 
    'l':'y', 
    'm':"z", 
    'n':'a', 
    'o':'b', 
    'p':'c', 
    'q':'d', 
    'r':'e', 
    's':'f', 
    't':'g', 
    'u':'h', 
    'v':'i',
    'w':'j',
    'x':'k', 
    'y':'l', 
    'z':'m'}

message = input("Let us encrypt your message...")

encypted_message = ''
for eng in message:
    if eng.lower() in rot13_dict:
        encypted_message += (rot13_dict[eng.lower()])
    
    if eng in ' .,':
        encypted_message += (eng)
      
print(encypted_message)