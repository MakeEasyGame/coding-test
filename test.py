# 더 맵게

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1 and scoville[0] < K:
        fst = heapq.heappop(scoville)
        scd = heapq.heappop(scoville)
        heapq.heappush(scoville, fst + (scd * 2))
        answer+=1

    return answer if scoville[0] >= K else -1
