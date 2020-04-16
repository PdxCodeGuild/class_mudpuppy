Dictionaries or ddicts provide an unordered, mutable, sequence of ke value pairs or a mapping between key and values. For more information check the official docs.

Dict literals are written with curl brackets and key-value pairs defined with colons and separated by commas.
{'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
{'David': ['day'], 'Sheri': ['day', 'night']} #Sheri is the key, you get a list with two strings

#You can't use a dictionary as a dictionary for keys. 
#CANNOT HAVE THE SAME KEY FOR TWO DIFFERENT VALUES.

product_to_price = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
print(product_to_price['grapes'])

print(product_to_price[1.0])

product_to_price['apple'] = 300

print(product_to_price['apple'])

ptoduct_to_price['avacado'] = 50000000

print(product_to_price['avacado'])

if 'apple' in product_to_price:
    print('apple' + str(product_to_price['apple']))

product_to_price.update({'banana': 0.25})
print(product_to_price)

print(list(product_to_price.keys()))
print(list(product_to_price.values()))
print(list(product_to_price.items()))

You can call sorted () on the results if you need a stable order. Dictionaries are naturally unordered; there is no guarantee the same order wil come out at each call

names_colors = [('alice', 'red'), ('david', 'green')]
new_dict = dict(names_and_colors)
print(new_dict)

---------------------------------------------------------------------------

import random
x = 5
def fun(num):
    y=10
    msg = "hello"
    return num+x
mynum = func(7)

print() needs to be within the scope of the function otherwise it will not print.
it will print unidentified scope instead.