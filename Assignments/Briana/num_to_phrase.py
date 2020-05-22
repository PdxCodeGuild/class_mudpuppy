ones_dict = {

0: '',
1: 'one',
2: 'two',
3: 'three',
4: 'four',
5: 'five',
6: 'six',
7: 'seven',
8: 'eight',
9: 'nine'
}

teens_dict = {

10: 'ten',
11: 'eleven',
12: 'twelve',
13: 'thirteen',
14: 'fourteen',
15: 'fifteen',
16: 'sixteen',
17: 'seventeen',
18: 'eighteen',
19: 'nineteen'
}

tens_dict = {

0: '',
2: 'twenty',
3: 'thirty',
4: 'forty',
5: 'fifty',
6: 'sixty',
7: 'seventy',
8: 'eighty',
9: 'ninety'
}

hundreds_dict = {

1: 'one hundred',
2: 'two hundred',
3: 'three hundred',
4: 'four hundred',
5: 'five hundred',
6: 'six hundred',
7: 'seven hundred',
8: 'eight hundred',
9: 'nine hundred'
}

while True:
        user_input = int(input("What number would you like to convert? "))

        if user_input <= 9:
                phrase = ones_dict[user_input]
                print(phrase)

        elif 10 <= user_input <= 19:
                phrase = teens_dict[user_input]
                print(phrase)

        elif 20 <= user_input <= 99:
                tens_value = user_input // 10
                ones_value = user_input % 10
                print(tens_dict[tens_value] + ones_dict[ones_value])

        elif user_input >= 100:
                hundreds_value = user_input // 100
                tens_value = (user_input % 100) // 10
                ones_value = user_input % 10
                print(hundreds_dict[hundreds_value] + tens_dict[tens_value] + ones_dict[ones_value])

        elif user_input < 1 or user_input >= 1000:
                print("Enter number 0-999: ")

        run_again = input( "Want to convert another number? y/n " )
    
        while run_again != "n" and run_again != "y":
                run_again = input( " Want to convert another number? y/n " )
        if run_again == 'n':
                break