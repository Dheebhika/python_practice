def climbing_leader_board(scores, alice):
    scores = list(set(scores))
    scores.sort(reverse=True)

    return first_approach(scores, alice)


def first_approach(scores, alice):
    result = []
    d = {}
    scores_count = len(scores)
    for i in range(0, scores_count):
        dictionary = {scores[i]: i + 1}
        d.update(dictionary)
    alice_count = len(alice)
    for i in range(0, alice_count):
        result.append(binarySearch(scores, alice[i])+1)
    return result


def binarySearch(arr, element):
    # assumption arr already sorted in desc
    start = 0
    end = len(arr) - 1
    while end - start > 1:
        mid = int((start + end) / 2)
        if element == arr[mid]:
            return mid
        if element < arr[mid]:
            start = mid
        elif element > arr[mid]:
            end = mid
    if element >= arr[start]:
        return start
    if element < arr[end]:
        return end + 1

    return start + 1


result_ = climbing_leader_board([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102])
print(result_)

# def array_elements(arr, element):
#     if element >= arr[0]:
#         return 0
#     if element <= arr[1]:
#         return 2
#     else:
#         return 1
#

# arr = [80, 70, 60]
# element = 55
# #
# result = array_elements(arr, element)
# print(result)

# binaryResult = binarySearch(arr, element)
# print(binaryResult)
