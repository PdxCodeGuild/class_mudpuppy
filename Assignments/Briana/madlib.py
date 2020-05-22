 # from random import choice
# # or
# # import random
# # random.choice()
#
# # a_list = ['a' ,'b' ,'c', 'd']
#
# def chooce(a_list):
#     rand_item = choice(a_list)
#     a_list.remove(rand_item)
#     # this command ^^ removes items from list that have already been used
#     return rand_item
#
# def main():
#     user_input = []
#
#     promts = [
# '\nGive me an antonym for \'data\': ',
#  'Tell me an adjective: ',
#  'Give me a sciency buzzword: ',
#  'A type of animal (plural): ',
#  'Some Sciency thing: ',
#  'Another sciency thing: ',
#  'Sciency adjective: ',
# ]
#
# while True:
#     for prompt in promts:
#         user_input.append(input(prompt))
#
#     madlib = f'\n{choose(user_input)} scientist job description: Seeking a {choose(user_input)} engineer, able to work on {choose(user_input)} projects with a team of {choose(user_input)} Key responsibilities: Extract patterns from {choose(user_input)}Optimize {choose(user_input)}Transform {choose(user_input)} into {choose(user_input)} material.'
#
#
# print(madlib)
#
# if(input('\nWould you like to make another (y/n): ').lower()!= 'y'):
#     print('no worries. \n')
#     # break
# main()


while True:

    import random


    adjectives_input = input( " Insert two adjectives. " )

    adj_list = adjectives_input.split ( ", " )

    adj_shuffle = random.shuffle(adj_list)


    place_input = input( " Insert three places. " )

    place_list = place_input.split ( ", " )

    place_shuffle = random.shuffle(place_list)


    verb_input = input( " Insert three verbs. " )

    verb_list = verb_input.split ( ", " )

    verb_shuffle = random.shuffle(verb_list)


    name_input = input( " Insert name. " )

    unit_of_time_input = input( " Insert plural unit of time. " )

    direction_input = input( " Insert direction. " )

    readlib = input( " Would you like to read the Madlib? " )

    if readlib == "yes":
        print (f"Once upon a time, there was a {adj_list[0]} gnome in the middle of a {adj_list[1]}  {place_list[0]}. On this particular day, the gnome was {verb_list[0]}ing around the {place_list[1]} waiting for his dear friend, {name_input}. After several {unit_of_time_input} of waiting, the gnome began to {verb_list[1]}. Worried that something wonderful had happened to his friend, the gnome quickly {verb_list[2]}ed to the nearest {place_list[2]} and yelled for help. The sky came falling {direction_input} and nothing was ever the same. The End. ")

  
    run_again = input("Would you like to complete another Madlib? ")
    
    while run_again != "no" and run_again != "yes":
        run_again = input("Would you like to complete another Madlib? ")
    if run_again == 'no':
        break