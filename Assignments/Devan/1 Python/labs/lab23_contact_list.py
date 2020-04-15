import os

BASE = os.path.dirname(os.path.abspath(__file__))
CSV = "contacts.csv"

contacts = []

with open(os.path.join(BASE, CSV)) as f:
    lines = f.readlines()
    header = lines[0].strip().split(",")
    print(header)
    for line in lines[1:]:
        line = line.strip().split(",")
        contact = dict(zip(header, line))
        # contact = {header[i]: line[i] for i in range(len(line))}
        contacts.append(contact)
    print(contacts)
