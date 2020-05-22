# operation_input = input('What is the operation you would like to perform? ')
# number_input = int(input('What is the first number? '))
# number2_input = int(input('What is the second number? ')) 


# if operation_input == '+':
#     answer = ((number_input)+(number2_input))
# if operation_input == '-':
#     answer = ((number_input)-(number2_input))
# if operation_input == '*':
#     answer = ((number_input)*(number2_input))
# if operation_input == '/':  
#     answer = ((number_input)/(number2_input))
# print(answer)

# Version 2

i = 1
while True:

    operation_input = input('What is the operation you would like to perform? ')
    number_input = input('What is the first number? ')
    number2_input = int(input('What is the second number? ')) 
    
    if operation_input == '+':
        answer = ((int(number_input))+(number2_input))
        
    if operation_input == '-':
        answer = ((int(number_input))-(number2_input))
        
    if operation_input == '*':
        answer = ((int(number_input))*(number2_input))
        
    if operation_input == '/':
        answer = ((int(number_input))/(number2_input))
        i += 1
        
    else:
        number_input == "done"
        print(answer)
        i += 1
        break
        




# i = 1
while True:
    operation_input = input('What is the operation you would like to perform? Enter done to quit ')
    if operation_input == 'done':
      break
    number_input = int(input('What is the first number? '))
    number2_input = int(input('What is the second number? ')) 
    if operation_input == '+':
        answer = number_input + number2_input
    elif operation_input == '-':
        answer = number_input - number2_input
    elif operation_input == '*':
        answer = number_input * number2_input
    elif operation_input == '/':
        answer = number_input / number2_input
        # i += 1
    # else:
    #   number_input == "done"
    print(answer)
    # break





# Version 3 (optional)
# Allow the user to enter a full arithmetic expression and use eval to evaluate it.