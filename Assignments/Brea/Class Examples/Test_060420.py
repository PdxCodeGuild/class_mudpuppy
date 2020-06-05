from flask import Flask
import emoticon_gen as e
import re
context = {
    'animal': 'giraffe',
    'color': 'yellow',
    'height': 'tall'
    }

def render(html_file, context):
    #html_file = "I saw a animal."
    #context = {'animal': 'giraffe'}
    with open(html_file, 'r') as f:
    text = f.read()
        #I saw a {{animal}}. It was a {{color}} {{animal}}. The {{color}} {{animal}} was {{height}}.
    print(text)
    for key, value in context.items():
        print(key, value)
        text = text.replace(key, value)
    return(text)
    #I saw a giraffe. It was a yellow giraffe. The yellow giraffe was tall.