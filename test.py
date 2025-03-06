# 숫자의 표현

def solution(n):
    answer = 1
    cnt = 2

    while sum(range(1, cnt+1)) <= n:
        nums = range(1, cnt+1)
        if sum(map(lambda x: (n - sum(range(1, cnt+1))) // cnt + x, nums)) == n:
            answer+=1

        cnt+=1

    return answer
