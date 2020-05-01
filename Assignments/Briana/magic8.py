import random
print ("Welcome to Magia Pellota Ocho")
while True:
    print ("Pedirme cualquier cosa")
    user = input()
    
    magic_answer_choices = ["por supuesto que si" , "dios mio no" , "con suerte" , "Desgraciado!"]
    predictions = random.choice(magic_answer_choices)
    print(predictions)

    # run_again = input("Quieres pedirme otro pregrunta? ")
    # if run_again == 'no':
    #     break
    # if run_again != "si":
    #     print("Invalid Input")


    run_again = input( " Quieres pedirme otro pregrunta? " )
    
    while run_again != "no" and run_again != "si":
        run_again = input( " Quieres pedirme otro pregrunta? " )
    if run_again == 'no':
        break