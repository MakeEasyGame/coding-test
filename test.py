# 오픈채팅방

def solution(record):
    answer = []
    lst = []
    dict = {}
    for r in record:
        info = r.split(' ')
        if info[0] == 'Enter':
            dict[info[1]] = info[2]
            lst.append(f'{info[1]} 님이 들어왔습니다.')
        elif info[0] == 'Leave':
            lst.append(f'{info[1]} 님이 나갔습니다.')
        else:
            dict[info[1]] = info[2]
    for i in lst:
        s = i.split(' ')
        answer.append(dict[s[0]]+s[1]+' '+s[2])
    return answer
