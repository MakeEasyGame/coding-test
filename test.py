# 압축

def solution(msg):
    w = ''
    dict = {i: ord(i)-64 for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    answer = []
    for c in msg:
        print(w, c)
        if w + c in dict.keys():
            w = w + c
        else:
            dict[w + c] = max(dict.values()) + 1
            answer.append(dict[w])
            w = c
    answer.append(dict[w])
    return answer
