def find_number_sort():
    read_input = input()
    array = list(read_input)
    sort = sorted(array)
    reverse_sort = list(reversed(sort))
    if array == sort:
        print("Ascending")
    elif array == reverse_sort:
        print("Descending")
    else:
        print("Neither")


find_number_sort()
