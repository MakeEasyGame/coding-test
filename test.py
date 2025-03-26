# [3차] N진수 게임

def solution(n, t, m, p):
    answer, nums = '', ''
    cnt, idx = 0, 0
    while cnt < p + m * t:
        num = str(to_base(cnt, n))
        nums += num[idx]
        idx+=1
        if idx >= len(num):
            cnt+=1
            idx=0

    answer = ''.join(map(lambda x: nums[x-1], (map(lambda x: p + m * x, range(t)))))
    return answer

def to_base(num, base):
    digits = "0123456789ABCDEF"
    result = ""
    if num == 0:
        return "0"
    while num > 0:
        result = digits[num % base] + result
        num //= base
    return result

print(solution(16,16,2,1))