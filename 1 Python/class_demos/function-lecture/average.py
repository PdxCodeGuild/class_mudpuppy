# is it possible to compute the average using reduce?
# perhaps...

def reduce_list_to_value(fn, starting_value, values):
    accumulator = starting_value
    for val in values:
        accumulator = fn(accumulator, val)
    
    return accumulator


xs = [1,2,3,4,5]

def average(xs):
    sum = 0.0
    for x in xs:
        sum += x

    return sum / len(xs)


def average2(xs):
    return reduce_list_to_value(lambda acc, val: acc + val / len(xs), 0, xs)

print(average2(xs))