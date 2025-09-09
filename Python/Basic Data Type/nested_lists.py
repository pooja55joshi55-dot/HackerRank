if __name__=='__main__':
    data= list()
    score= list()
    for i in range(int(input())):
        name = str(input())
        marks = float(input())
        score.append(marks)
        data.append([name,marks])

    score = sorted(set(score))
    data.sort(key=lambda x: (x[1], x[0]))
    for block in data: 
        if block[1] == score[1]:
            print(block[0])

