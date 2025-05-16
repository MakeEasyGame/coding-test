# 숫자 변환하기

def solution(x, y, n):
    queue = [(x, 0)]
    visited = set()
    visited.add(x)
    idx = 0
    while idx < len(queue):
        current, cnt = queue[idx]
        idx += 1
        if current == y:
            return cnt
        for i in (current+n, current*2, current*3):
            if i <= y and i not in visited:
                visited.add(i)
                queue.append((i, cnt + 1))

    return -1
