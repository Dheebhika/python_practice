def icecreamParlor(m, arr):
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == m:
                result = [i + 1, j + 1]

        break

    display(result)


def display(result):
    print(result)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)
