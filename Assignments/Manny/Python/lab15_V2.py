tens_dict ={  
9 : "ninety",
8 : "eighty",
7 : "seventy",
6 : "sixty",
5 : "fifty",
4 : "forty",
3 : "thirty",
2 : "twenty",
0 : ''
}

ones_dict = {
1 : 'one',
2 : 'two',
3 : 'three',
4 : 'four',
5 : 'five',
6 : 'six',
7 : 'seven',
8 : 'eight',
9 : 'nine',
0 :  ''
}

teens = {
10 : "ten",    
11 : "eleven",
12 : "twelve",
13 : "thirteen",
14 : "fourteen",
15 : "fifteen",
16 : "sixteen",
17 : "seventeen",
18 : "eightteen",
19 : "nineteen"
}

hundreds_dict = {
1 : "one-hundred",
2 : "two-hundred",    
3 : "three-hundred",
4 : "four-hundred",
5 : "five-hundred",
6 : "six-hundred",
7 : "seven-hundred",
8 : "eight-hundred",
9 : "nine-hundred",
}
num = int(input("Please enter a number: "))
if num < 10:
    
    ones_digit = num % 10

    print(f"{ones_dict[ones_digit]} ")
elif num > 10 and num < 21:
    print(f"{teens[num]}")

elif num > 21 and num < 100:
    ones_digit = num % 10
    tens_digit = num // 10
    print(f"{tens_dict[tens_digit]}-{ones_dict[ones_digit]}") 

elif num >= 101 and num < 999:
    hundreds_digit = num // 100
    ones_digit = num % 10
    tens_digit = num // 10
    print(f"{hundreds_dict[hundreds_digit]}{tens_dict[tens_digit]}{ones_dict[ones_digit]}")