# units = {
#     "ft": .3048,
#     "mi": 1609.34,
#     "m": 1,
#     "km": 1000,
#     "yd": .9144,
#     "in": .0254,

# }

# while True:
#     distance = float(input("Enter a number:"))
#     unit = input("Enter the Unit:")

#     while unit not in units:
#         unit = input(f"Enter the unit: {list(units.keys())} \n")
#     meters = units[unit] * distance


#     units = {
#         "ft": .3048,
#         "mi": 1609.34,
#         "m": 1,
#         "km": 1000,
#         "yd": .9144,
#         "in": .0254,

#     }

#     print(f"{distance}{unit} is {meters}m")

#     answer = input("Would you like to add another unit?")

#     if answer == "yes":
#         unit = input("Enter the unit:")
#         conversion = float(input("Enter the conversion:"))

#         units[unit] = conversion
#     else:
#         print("Thank you fam")
#         break
# number = input("What is the distance in ft? : ")
# unit = input("What are the units? : ")

units = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254,
}

# while True:
distance = float(input("Enter a number:"))
# unit = input("Enter the Unit:")

    # # while unit not in units:
unit = input(f"Enter the unit: {list(units.keys())} \n")
meters = units[unit] * distance

print(f"{distance}{unit} is {meters}m")

answer = input("Would you like to add another unit? (Type yes or no").lower()

if answer == "yes":
    distance = float(input("What is the Distance? :"))
    starting = str(input(f"What are your starting units?  : {list(units.keys())} \n "))
    ending = str(input(F"What units would you like to convert to? : {list(units.keys())} \n "))
    converted = (distance * ((units[starting])/units[ending]))
    print(f"{distance}{starting} is {converted}{ending}")
else:
    print("Thank you fam")
      