from collections import Counter


def isValid(s):
    array = []
    array1 = []
    counter = Counter(s)
    dictionary = dict(counter)
    print(dictionary)
    for values in dictionary.values():
        array.append(values)
    print(array)
    if len(set(array)) == 1:
        return "YES"
    elif len(set(array)) >= 3:
        return "NO"
    elif len(set(array)) == 2:
        counter1 = Counter(array)
        dictionary1 = dict(counter1)
        print(dictionary1)
        for values in dictionary1.values():
            array1.append(values)
        print(array1)
        # sort = sorted(array)
        # print(sort)
        # subtract = sort[len(sort) - 1] - sort[0]
        # print(subtract)
        # if subtract == sort[0] or subtract == sort[len(sort) - 1]:
        #     return "YES"

    # remove_duplicate = set(array)
    # sorted_value = sorted(remove_duplicate)
    # print(sorted_value)
    # if len(remove_duplicate) == 2 and sorted_value[1] == sorted_value[0] + 1:
    #     print("YES")
    # else:
    #     print("NO")


s = "abss"
result = isValid(s)
print(result)
