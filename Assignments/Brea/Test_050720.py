#Test Examples, May 7th, 2020
import random
import re

def make_emoticon: 
    eye_choices = ':;B'
    nose_choices = '>-'
    mouth_choices = 'DC)O'
    return random.choice(eye_choices) + random.choice(nose_choices) + random.choice(mouth_choices)  

emoticon = make_emoticon()

template_vars_dict = {'emoticon_template_var': emoticon, 'greeting_template_var': 'Welcome'}

with open("emoticon_base.html", "r") as f:
    html_string = f.read()
    delim = re.compile("{{(.*?)}}")

found_vars = re.findall(delim, html_string)

print(html_string.repace("{{" + foundvars[1] + "}}", emoticon)) #finding the stuff between {{}}

for one_var in found_vars:
    html_string = html_string.replace("{{" + one_var + "}}", template_vars_dict.get(one_var, '')) #replace stuff in our html file, replace everything we found between double curlies

# print(html_string.replace("{{",  "").replace("}}", ""). replace("emoticon_template_var", emoticon)).replace("greeing_template_var", "Welcome to our emoticon generator!"))