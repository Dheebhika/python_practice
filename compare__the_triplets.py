def compareTriplets(a, b):
    count_of_alice = 0
    count_of_bob = 0
    for i in range(0, 3):
        if a[i] > b[i]:
            count_of_alice += 1
        elif a[i] < b[i]:
            count_of_bob += 1
    print(count_of_alice)
    print(count_of_bob)


a = [1, 2, 3]
b = [3, 2, 1]
compareTriplets(a, b)
