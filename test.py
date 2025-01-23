def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        count = 0
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                count += yearning[name.index(photo[i][j])]
        
        answer.append(count)

    return answer