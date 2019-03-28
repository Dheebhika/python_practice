from collections import Counter


def count_n_times_char(string, number):
    # n = str(input())
    result = []
    lower_case = string.lower()
    print(lower_case)
    # element = int(input())
    # print(x)
    array = lower_case.split(",")
    print(array)
    counter = Counter(array)
    dictionary = dict(counter)
    print(dictionary)
    for key, value in dictionary.items():
        if number == value:
            result.append(key)
            final = " ".join(result)
    return final


string = "A,a,b,B,c"
number = 2

print(count_n_times_char(string, number))
