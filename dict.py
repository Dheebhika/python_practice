from collections import defaultdict

d = defaultdict(list)
array = str(input()).split()
x = array[0]
y = array[1]
a = []
for i in range(0, int(x)):
    d[input()].append(str(i + 1))

for j in range(0, int(y)):
    a.append(input())

for j in range(0, int(y)):
    var=d[a[j]]
    if not var:
        print("-1")
    else:
        print(' '.join(var))
