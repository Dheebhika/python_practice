def sum_of_digits_in_factorial(number):
    if number == 1:
        return 1
    else:
        return number * sum_of_digits_in_factorial(number - 1)


number = 5
result = sum_of_digits_in_factorial(number)
array = list(str(result))
sum = 0
for i in array:
    array = int(i)
    sum = sum + array
print(sum)
