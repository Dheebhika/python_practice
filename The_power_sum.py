def powerSum(X, N):
    dictionary = dict()
    count = 0
    array = []
    for keys in range(1, X + 1):
        dictionary[keys] = keys ** N
    if X in dictionary.values():
        count += 1

    for values in dictionary.values():
        if values < X:
            array.append(values)

    value = countWays(X, N)
    return value


def countWaysUtil(X, N, num):
    val = (X - pow(num, N))
    if (val == 0):
        return 1
    if (val < 0):
        return 0

    return countWaysUtil(val, N, num + 1) + countWaysUtil(X, N, num + 1)



def countWays(X, N):
    return countWaysUtil(X, N, 1)


X = int(input())

N = int(input())

result = powerSum(X, N)
print(result)
