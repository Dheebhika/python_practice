if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        value = input().split(" ")
        command = value[0]
        if command == 'insert':
            list.insert(int(value[1]), int(value[2]))
        if command == 'print':
            print(list)
        if command == 'remove':
            list.remove(value[1])
        if command == 'append':
            list.append(value[1])
        if command == 'sort':
            list.sort()
        if command == 'pop':
            list.pop()
        if command == 'reverse':
            list.reverse()



