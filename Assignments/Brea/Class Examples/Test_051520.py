#Test Examples May 15th, 2020

def get_ticket():
    output = []
    for in in range(6):
        output.append(random.randint(1, 99))
    return [random.randint(1, 99) for i in range(6)]

winning_ticket = get_ticket()
for i in range(100):
    matches = 0
    user_ticket = get_ticket()
    for i in range(len(winning_ticket)):
        if winning_ticket[i] == user_ticket[i]:
            matches += 1
        print(matches)
