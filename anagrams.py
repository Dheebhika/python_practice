def check_anagrams():
    first = input()
    second = input()
    replace = second.replace(" ", "")
    array1 = list(first)
    array2 = list(replace)
    # if set(array1) == set(array2) and len(array1) == len(array2):
    if sorted(array1) == sorted(array2):
        return "TRUE"
    else:
        return "FALSE"


result = check_anagrams()
print(result)
