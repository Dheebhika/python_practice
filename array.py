array = [[11, 12, 5, 2], [15, 6, 10, 8], [10, 8, 12, 5], [12, 15, 8, 6]]
a = 0
b = 0
# for rows in array:
#     for columns in rows:
#         print(columns, end=" ")
#     print()
# print(array[3][2])
for i in range(0, 4):
    for j in range(0, 4):
        print(array[i][j], end=" ")
    print()

for i in range(0, 4):
    for j in range(0, 4):
        if i == j:
            print(array[i][j])
            a += array[i][j]
print(a)
for i in range(0, 4):
    for j in range(0, 4):
        if i == 4 - j - 1:
            print(array[i][j])
            b += array[i][j]
print(b)
difference = abs(a-b)
print(difference)
