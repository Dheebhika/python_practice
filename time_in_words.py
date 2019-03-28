def timeInWords(h, m):
    numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
               10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 16: 'sixteen', 17: 'seventeen',
               18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two', 23: 'twenty three',
               24: 'twenty four', 25: 'twenty five', 26: 'twenty six', 27: 'twenty seven', 28: 'twenty eight',
               29: 'twenty nine'}
    time = []
    words = {1: 'one minute past', 15: 'quarter past', 30: 'half past'}
    if m in words.keys():
        time.append(words[m])
        time.append(numbers[h])
        return time
    if m == 00:
        time.append(numbers[h])
        time.append("o' clock")
        return time
    if m == 45:
        time.append('quarter to')
        time.append(numbers[h + 1])
        return time
    if (2 <= m <= 14) or (16 <= m <= 29):
        time.append(numbers[m])
        time.append('minutes past')
        time.append(numbers[h])
        return time
    if (31 <= m <= 44) or (46 <= m <= 59):
        time.append(numbers[60 - m])
        time.append('minutes to')
        time.append(numbers[h + 1])
        return time


h = int(input())

m = int(input())

result = timeInWords(h, m)
for i in range(0, len(result)):
    print(result[i], end=" ")
