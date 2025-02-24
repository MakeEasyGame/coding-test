from collections import Counter

def solution(participant, completion):
    answer = ""
    return list((Counter(participant) - Counter(completion)).elements())[0]