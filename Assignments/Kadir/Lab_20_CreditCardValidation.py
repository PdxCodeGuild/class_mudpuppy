#Lab_20_CreditCardValidation
#function of list 

def credit_checker(card_number):

    card_list = list(card_number) # convert string to list of ints
    
    last_digit = card_list.pop(-1) # slice off and save digit
    
    card_list.reverse() # reverse card list
    
    for i in range(len(card_list)):
        card_list[i] = int(card_list[i]) # change string to int

    for i in range(0,(len(card_list)),2): # double every other element
        card_list[i] *= 2

    for i in range(len(card_list)): # subtract nine from numbers over nine
        if card_list[i] > 9:
            card_list[i] -= 9
    
    sum_variable = sum(card_list) #  sum of numbers in a list

    sum_variable = list(str(sum_variable)) # converting sum variable into string list
   
    if sum_variable[-1] == last_digit: # checking to see if second digit of sum 
        return True
    
    return False

input_string = "4556737586899855"

print(credit_checker(input_string))

# Take the second digit of that sum.
#If that matches the check digit, the whole card number is valid.