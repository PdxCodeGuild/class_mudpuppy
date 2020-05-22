# employee_availability = {
# "lisa": ["Mon"], # string
# "al": ["Tues", "Wed", "Thurs"], # list
# "anthony": ["Mon", "Tues", "Wed", "Thurs", "Fri"] # list
# }
# # keys: "lisa", "al", "anthony"
# # value: "Mon", ["Tues", "Wed", "Thurs"], ["Mon", "Tues", "Wed", "Thurs", "Fri"]
#
# # how many days will Al work in a year?
# # 52 weeks in a year multiplied by the number of days worked each week (3)
# worked_days = 52 * len(employee_availability["anthony"])
# print(worked_days)


#
#
person = {
    "first_name": "Stan",
    "last_name": "Scott",
    "age": 28,
    "height": "4ft 11in",
    "fav_foods":['pizza','wings','lamb burgers'],
}

person["fruit"] = "apple"

person.pop("fav_foods")

key = list(person.keys())

print(person.keys())
print(person.values())

print(person.get("pet","no pet found"))

# LOOP WITH DICTIONARIES

# print(person["first_name"])
# #print(person[first_name])

# # food = person["fav_food"][1]
# # print(food)

# for banana in person
# print(f"{key}: {person[key}]}")




# Dictionaries or ddicts provide an unordered, mutable, sequence of ke value pairs or a mapping between key and values. For more information check the official docs.
# # Dict literals are written with curl brackets and key-value pairs defined with colons and separated by commas.
# {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
# {'David': ['day'], 'Sheri': ['day', 'night']} #Sheri is the key, you get a list with two strings
# #You can't use a dictionary as a dictionary for keys. 
# #CANNOT HAVE THE SAME KEY FOR TWO DIFFERENT VALUES.
# product_to_price = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
# print(product_to_price['grapes'])
# print(product_to_price[1.0])
# product_to_price['apple'] = 300
# print(product_to_price['apple'])
# ptoduct_to_price['avacado'] = 50000000
# print(product_to_price['avacado'])
# if 'apple' in product_to_price:
#     print('apple' + str(product_to_price['apple']))
# product_to_price.update({'banana': 0.25})
# print(product_to_price)
# print(list(product_to_price.keys()))
# print(list(product_to_price.values()))
# print(list(product_to_price.items()))
# # You can call sorted () on the results if you need a stable order. Dictionaries are naturally unordered; there is no guarantee the same order wil come out at each call
# names_colors = [('alice', 'red'), ('david', 'green')]
# new_dict = dict(names_and_colors)
# print(new_dict)