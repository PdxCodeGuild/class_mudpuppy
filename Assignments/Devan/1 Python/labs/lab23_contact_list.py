import os

BASE = os.path.dirname(os.path.abspath(__file__))
CSV = "contacts.csv"

contacts = []

with open(os.path.join(BASE, CSV)) as f:
    lines = f.readlines()
    header = lines[0].strip().split(",")

    for line in lines[1:]:
        line = line.strip().split(",")
        contact = dict(zip(header, line))
        # contact = {header[i]: line[i] for i in range(len(line))}
        contacts.append(contact)

for p in contacts:
    print(p.get('name') + "'s favorite food is " + p.get('food') + " and they enjoy " + p.get('hobby'))
