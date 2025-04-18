# 2 x n 타일링

def solution(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, (a + b) % 1000000007
    return b