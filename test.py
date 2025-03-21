# [1차] 캐시

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)
    
    for city in cities:
        city = city.lower()
        if city in cache: # hit
            cache.remove(city)
            answer += 1
        else: # miss
            answer += 5

        cache.append(city)

    return answer
