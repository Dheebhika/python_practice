# 1. Get input list of numbers from User
# 2. Largest no
# 3. Sort
# 4. reverse
# 5. square no of elements


def read_list():
    list_values = []
    length = int(input())
    for i in range(length):
        value = int(input())
        list_values.append(value)
    print("list:", list_values)
    return list_values


def sort_list(list_values):
    list_values.sort()
    print("sorted_list:", list_values)
    return


def reverse_list(list_values):
    list_values.reverse()
    print("reversed_list:", list_values)
    return


def square_list(list_values):
    square_values = [values ** 2 for values in list_values]
    print("square_values:", square_values)
    return


lists = read_list()
sort_list(lists)
reverse_list(lists)
square_list(lists)
