# 구명보트

from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse=True))

    while people:
        p = people.popleft()
        answer += 1

        if people and limit - p >= people[-1]:
            people.pop()

    return answer
