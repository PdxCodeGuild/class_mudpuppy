temp_input = temp_input = float(input('enter a temperature: '))
unit = input('enter a unit: ')
convert_to_unit = input('enter a unit to convert to: ')
converted_temp = ""

# eq3 = converted_temp = convert_to_f(temp_input)
# eq2= converted_temp = convert_to_c(temp_input)


def convert_to_c():
    return ((9 / 5) * temp_input) + 32
convert_to_c()

def convert_to_f():
    return (5 / 9) * (temp_input - 32)
convert_to_f()

# eq3 = convert_to_f(temp_input)
# eq2= converted_temp = convert_to_c(temp_input)
def main():
#   temp_input = float(input('enter a temperature: '))
#   unit = input('enter a unit: ')
#   convert_to_unit = input('enter a unit to convert to: ')
# main(enter1, enter2)
  if convert_to_unit in ('c', 'C'):
    converted_temp = convert_to_f()
    print(converted_temp, "C")
  elif convert_to_unit in ('f', 'F'):
    converted_temp = convert_to_c()
    print(converted_temp, "F")
  else:
    print('no temp entered')
main()
print(converted_temp)