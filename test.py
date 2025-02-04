def solution(nums):
    answer = 0
    pokemon = len(set(nums))

    answer = min(pokemon, len(nums)//2)

    return answer