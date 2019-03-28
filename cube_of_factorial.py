def cube_of_factorials(number):
    array = []
    sum_of_array = 0
    first_number = 0
    second_number = 1
    array.append(first_number)
    array.append(second_number)
    for values in range(2, number + 1):
        third_number = first_number + second_number
        array.append(third_number)
        first_number = second_number
        second_number = third_number
    for i in range(0, len(array)):
        sum_of_array = sum_of_array + (array[i] ** 3)
    print(sum_of_array)


number = 4
cube_of_factorials(number)
