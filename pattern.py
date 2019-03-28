def staircase(n):
    for i in range(0, n):
        for j in range(i + 1, n):
            print(" ", end="")
        for k in range(0, i + 1):
            print("#", end="")
        print()


if __name__ == '__main__':
    n = int(input())

staircase(n)

#
# for i in range(0,6):
#     print (i)
