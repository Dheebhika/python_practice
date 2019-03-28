if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    array = list(set(arr))
    array.sort()
    array.reverse()

    print(array[1])

#
# if __name__ == '__main__':
#     N = int(input())
#     list=[]
#     list.insert(0,5)
#     print(list)
