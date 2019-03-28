from collections import Counter


def function():
    n = str(input())
    print(n)
    element = int(input())
    print(n)
    a = n.split(",")
    print(a)
    b = Counter(a)
    c = dict(b)
    print(c)
    for key, value in c.items():
        if element == value:
            print(key)


function()
