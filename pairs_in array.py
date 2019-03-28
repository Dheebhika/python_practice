def pairs_in_array(array, number):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            result = []
            if array[i] + array[j] == number:
                result.append(array[i])
                result.append(array[j])
                print(result)


array = [1, 3, 7, 4, 5, 6]
number = 10
pairs_in_array(array, number)
