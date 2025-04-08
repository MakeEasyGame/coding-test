# 스킬트리

import math

def solution(fees, records):
    answer = []
    total_parking = {}
    in_time = {}
    for r in records:
        s = r.split(' ')
        time = list(map(lambda x: int(x), s[0].split(':')))
        time = time[0] * 60 + time[1]
        if s[2] == "IN":
            if s[1] not in total_parking: total_parking[s[1]] = 0
            in_time[s[1]] = time
        else:
            if s[1] in in_time:
                total_parking[s[1]] += time - in_time[s[1]]
                in_time.pop(s[1], None)
    for t in in_time:
        total_parking[t] += 1439 - in_time[t]

    for p in sorted(total_parking.items()):
        if p[1] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((p[1] - fees[0]) / fees[2]) * fees[3])

    return answer

print(solution([180, 5000, 10, 600], 
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))