# a = '132 456 Wq  m e'
# b = list(a)
# s = b[0].swapcase()
# b[0] = s

# for i in range(0, len(a)):
#     if b[i] == ' ':
#         x = b[i + 1].swapcase()
#         b[i + 1] = x
# result = ''.join(b)
# print(result)

a = 'chris alan'
array = []
splits = a.split(" ")

for i in range(0, len(splits)):
    result = splits[i].capitalize()
    array.append(result)

final = ' '.join(array)
print(final)
