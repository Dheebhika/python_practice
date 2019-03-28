def sorted_sequence():
    read_input = input()
    split_input = read_input.split(",")
    sort_input = sorted(split_input)
    join_input = ",".join(sort_input)
    return join_input


result = sorted_sequence()
print(result)
