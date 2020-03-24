meters = {
    "feet": 0.3048,
    "miles": 1609.34,
    "meters": 1,
    "kilometers": 1000,
    "yards": 0.9144,
    "inches": 0.0254,
}
distance = input("What is the distance? ")
units = input("What are the recored units? ")
print(meters.get(units, 0) * int(distance)) 