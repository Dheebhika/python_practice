def rotLeft(a, d):
    rotate = a[-d%len(a):] + a[:-d%len(a)]
    # for i in range(0, d):
    #     rotate = a[1:] + a[:1]
    return rotate


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(result)
