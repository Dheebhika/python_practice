def read_list():
    list_values = []
    length = int(input())
    for i in range(length):
        value = int(input())
        list_values.append(value)
        # tuples = tuple(list_values)
    array=list_values[0]
    print(list_values)
    print("array[0]",array)

    return list_values


read_list()
