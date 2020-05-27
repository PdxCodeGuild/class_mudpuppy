import string

# taking items out of the function
name_list=[]
key_list=[]
# Removed unnecessary items
food_list=[]
# dict-{}
fav_food=[]
hobby_list=[]
punctuation=string.punctuation
letters = string.ascii_letters

with open('contacts.csv', 'r') as file:
    lines = file.read().strip().split('\n')
    # print(lines)
    for loop in lines:
        dad=loop.strip("ï»¿")
        dads = dad.split(',')
        name_list.append(dads)
   

for item in name_list:
    letter2= (item[0])
    # print(letter2)
    letter3 = (letter2[0])
    # for letter3 in letter2:
    letter4= letter2.strip("ï»¿")
    food_list.append(letter4)

    letter5=item[1]
    fav_food.append(letter5)

    letter6=item[2]
    hobby_list.append(letter6)


food_list.pop(0)
fav_food.pop(0)
hobby_list.pop(0)









'''
print(food_list) # name list
print(fav_food) #food list
print(hobby_list) #hobby list
'''


while True:
    choice=int(input("Enter a number:\n 1.Print Contacts\n 2.Create a New Contact\n 3.Delete Contact\n 4. Update a record"))
    one_dict={}

    # for i in range(len(food_list)):
    #     # one_dict={}
    #     one_dict["name"]=food_list[i]
    #     one_dict["favorite food"]=fav_food[i]
    #     one_dict["hobby"]=hobby_list[i]
    #     # print(one_dict)

    #     continue
    # else:
    #     pass
        

    # print(one_dict)
    def final(choice):
        if choice == 1:
    # one_dict={}
            for i in range(len(food_list)):
        # # one_dict={}
                one_dict["name"]=food_list[i]
                one_dict["favorite food"]=fav_food[i]
                one_dict["hobby"]=hobby_list[i]
                print(one_dict)

    #     continue
    # else:
    #     pass
        
        elif choice==2:
            user=int(input("How many contacts would you like to add?"))
            for i in range(user):
                contact=str(input("What's their name?")).strip().capitalize()
                food_list.append(contact)
                foodie=str(input("What's their favorite food?")).strip()
                fav_food.append(foodie)
                hobby=str(input("What's their hobby?")).strip()
                hobby_list.append(hobby)
                
            for i in range(len(food_list)):
        # one_dict={}
                one_dict["name"]=food_list[i]
                one_dict["favorite food"]=fav_food[i]
                one_dict["hobby"]=hobby_list[i]
                
                
                print(one_dict)

        elif choice==3:
            user2=str(input("Which contact would you like to delete?")).capitalize()
            # one_dict.pop(user2)
            food_list.remove(user2)
            # print(food_list)
            # print(one_dict)

            for i in range(len(food_list)):
                one_dict["name"]=food_list[i]
                one_dict["favorite food"]=fav_food[i]
                one_dict["hobby"]=hobby_list[i]
                
              

                print(one_dict)

        elif choice==4:
            for i in range(len(food_list)):
        # # one_dict={}
                one_dict["name"]=food_list[i]
                one_dict["favorite food"]=fav_food[i]
                one_dict["hobby"]=hobby_list[i]
                print(one_dict)
            

            user_4=str(input("Which key would you like to change?\n(Name\tFavorite Food\tHobby")).lower()
            user_42=str(input("For which contact would you like to change?")).capitalize()
            user_43=str(input("What would you like to change it to?")).lower()
            
            if user_4 == "name":

                res= [i.replace(user_42,user_43) for i in food_list]
                # print(res)
                for i in range(len(res)):
                    one_dict["name"]=res[i]
                    one_dict["favorite food"]=fav_food[i]
                    one_dict["hobby"]=hobby_list[i]
                
                
                    

            elif user_4=="favorite food":
                user_5=input("Which Food would you like to replace?").lower()
                # hello=one_dict.get(user_4,user_5).replace(user_5,user_43)
                print(one_dict)
                
                # res4=one_dict["name"]=user_42
                res2= [i.replace(user_5,user_43) for i in fav_food]
                # print(res2)
                # print(res4)
                
                for i in range(len(res2)):
                    one_dict["name"]=food_list[i]
                    one_dict["favorite food"]=res2[i]
                    one_dict["hobby"]=hobby_list[i]
                    print(one_dict)

            elif user_4=="hobby":
                user_6=input("Which hobby would you like to replace?").lower()
                res3= [i.replace(user_6,user_43) for i in hobby_list]
                # print(res)
                for i in range(len(res3)):
                    one_dict["name"]=food_list[i]
                    one_dict["favorite food"]=fav_food[i]
                   
                    one_dict["hobby"]=res3[i]
                    print(one_dict)
                
        else:
            ("Thank you, Come again soon!")
                







            
            # print(one_dict)
        # elif choice==4:
        #     user3=input("What would you like to update?\n(name,favorite food, or hobby").lower()
        #     # user2
        #     if user3=="name":
        #         one_dict[user3]=
        #         one_dict.update({user3})
    final(choice)

    







