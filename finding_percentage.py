if __name__ == '__main__':
    n = int(input())
    average = 0
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    array = student_marks[query_name]
    for i in range(0, len(array)):
        average = average + array[i]
    print(format(average / len(array), '.2f'))
