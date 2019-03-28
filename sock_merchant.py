ar = [10, 10, 20, 20]
result = 0
ar.sort()
for i in range(0, 4):
    if ar[0] == ar[1]:
        ar.pop(0)
        ar.pop(1)
    # else:
    #     ar.pop(i)
    #     result += 1
print(result)





