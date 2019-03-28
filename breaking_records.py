def breakingRecords(scores):
    best = scores[0]
    worst = scores[0]
    worst_count = 0
    best_count = 0

    for i in range(0, n):

        if scores[i] < worst:
            worst = scores[i]
            worst_count = worst_count + 1

        if scores[i] > best:
            best = scores[i]
            best_count = best_count + 1

    return [best_count, worst_count]


if __name__ == '__main__':
    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print(result)
