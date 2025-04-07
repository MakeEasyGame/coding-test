# 스킬트리

def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        skill_trees[i] = list(filter(lambda x: x in skill, skill_trees[i]))
        temp = 1
        s = ''.join(skill_trees[i])
        for j in range(len(s)):
            if s[j] != skill[j]:
                temp = 0
                break
        answer+=temp
    
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))