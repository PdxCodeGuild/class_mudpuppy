keep_going = True

while keep_going:
    userColor = input("Give me a color : ");
    userFood = prompt("Give me a food : ");
    userRhyme = prompt("Give a word that rhymes with ham : ");

    output = print(`Do you like ${userColor} ${userFood} and ham? \n
    I do not like them Sam-I-${userRhyme}`)
    
    input("Do you want to keep going? : ")
    if input == 'no':
        break

    
