def plusMinus(arr):
    negative = 0
    positive = 0
    zero = 0
    for values in arr:
        if values < 0:
            negative += 1

        if values > 0:
            positive += 1

        if values == 0:
            zero += 1
    display(positive / n)
    display(negative / n)
    display(zero / n)
    return


def display(number):
    print(format(number, '.6f'))
    return number


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    number = plusMinus(arr)
