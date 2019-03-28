def miniMaxSum(arr):
    minimum = 0
    maximum = 0
    arr.sort()
    for i in range(0, len(arr) - 1):
        minimum = minimum + arr[i]
    for i in range(1, len(arr)):
        maximum = maximum + arr[i]
    return [minimum, maximum]


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    result = miniMaxSum(arr)
    print(result)

