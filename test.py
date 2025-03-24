# 튜플

def solution(s):
    answer = []
    lst = list(map(lambda x: x.split(','), s[2:-2].split('},{')))
    
    s = sorted(lst, key=lambda x: len(x))
    
    for i in range(len(s)):
        if i>0: answer.append(int(*(set(s[i]) - set(s[i-1]))))
        else: answer.append(int(*s[i]))

    return answer
