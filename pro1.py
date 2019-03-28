def x(input):
    output = []
    for i in input:
        if i not in output:
            output.append(i)
    print(output)


if __name__ == '__main__':
    x([1, 2, 3, 4, 5, 11, 5, 1, 10, 3])
