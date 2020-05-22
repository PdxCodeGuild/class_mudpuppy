with open('contacts.csv', 'r') as file:
    lines = file.read()
    lines = lines.strip()
    lines = lines.split('\n')
    #print(lines)   # lines 1-3 are pulling out csv file, then reading it, after the .split converts to a list

# now lines is a list of our contacts and each contact iis its grouping of info. 
# for example ["manny, pizza, dancing", "brea, ice cream singing

contacts = [] # we know what we want contacts to looks like  {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},{'name':'sam', 'favorite fruit':'pineapple' 
keys = lines[0]
keys = keys.split(",")
lines = lines[1:] # slicing excluding index 0 and starting at index 1

for one_list in lines:
    onelist = one_list.split(",")
    one_dict = {}
    # contacts.append(one_dict)
    for index in range(len(onelist)):
        # key = keys[index]
        # var2 = onelist[index]
        
        # one_dict[key] = var2
        one_dict[keys[index]] = onelist[index]
    contacts.append(one_dict)    
        #one_dict["name"] = "manny"

   
print(contacts)