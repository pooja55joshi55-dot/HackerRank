if __name__ == '__main__':
    n = int(input())
    student_data = {}
    for i in range(n):
        name, *line = input().split()
        student_data[name] = list(map(float, line))

    want = str(input())
    if want in student_data:
        average = sum(student_data[want])/len(student_data[want])
        print(format(average, ".2f"))
