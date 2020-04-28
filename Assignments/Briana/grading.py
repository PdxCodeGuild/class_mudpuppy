while True:
    num = input("Enter a number: ")

    num = float(num)
      # promt user to submit numeric value when input calls for an integer and diff input is given

    if num > 100.0:
        print("YASS")
    if 100 > num > 97:
        print("A+")
    if num > 93 and num < 98:
        print("A")
    if num > 89 and num < 94:
        print("A-")


    if num > 87 and num < 90:
        print("B+")
    if num > 83 and num < 88:
        print("B")
    if num > 79 and num < 84:
        print("B-")


    if num > 77 and num < 80:
        print("C+")
    if num > 73 and num < 78:
        print("C")
    if num > 69 and num < 74:
        print("C-")


    if num > 67 and num < 70:
        print("D+")
    if num > 63 and num < 68:
        print("D")
    if num > 59 and num < 64:
        print("D-")


    if num > -1 and num < 60:
        print("F")


    run_again = input("Would you like to compute another grade? ")
    
    while run_again != "no" and run_again != "yes":
        run_again = input("Would you like to compute another grade? ")
    if run_again == 'no':
        break

     