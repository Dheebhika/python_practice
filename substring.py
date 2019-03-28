def count_substring(string, sub_string, count):
    result = count
    array = list(string)
    sub = string.find(sub_string)
    if sub >= 0:
        del array[sub]
        string = "".join(array)
        result += 1
        return count_substring(string, sub_string, result)
    else:
        return result


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string, 0)
    print(count)
