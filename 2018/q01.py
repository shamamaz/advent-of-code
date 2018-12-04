from aocd import data

def a(data):
    return sum([int(x) for x in data.split()])

def b(data):
    a = {}
    here = 0
    while not False:
        for x in data.split():
            a[here] = ''
            here += int(x)
            if here in a:
                return here
print(a(data))
print(b(data))
