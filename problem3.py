def function():
    n = str(input())
    a = list(n)
    a.sort()
    b = ''.join(a)
    if b == n:
        print("Yes")
    else:
        print("No")


function()
