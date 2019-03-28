def birthday(s, d, m):
    count = 0

    for i in range(0, n):
        j = 0
        sum = 0
        while j < m:
            sum = sum + s[i + j]
            j += 1
        if sum == d:
            count += 1
        if i + j == n:
            break

    return count


if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(result)
