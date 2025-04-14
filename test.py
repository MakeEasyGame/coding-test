# 택배상자

def solution(order):
    stack = []
    num = 1
    idx = 0
    while num <= len(order):
        stack.append(num)
        while stack and stack[-1] == order[idx]:
            stack.pop()
            idx+=1
            if idx == len(order):
                break
        num+=1

    return idx
