units = {'feet': .03048, 'miles': 1609.34, 'meters': 1, 'kilometers': 1000, 'yards': .9144, 'inches': .0254}

var1 = input('what is the distance ')
var2 = input('what are the units ')

formula = int(var1) * units[var2]

print(f"{var1} {var2} is {formula} meters")