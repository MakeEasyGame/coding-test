def solution(arr):
    answer = []
    for i in range(len(arr)):
        n = i - 1
        if n >= 0:
            if arr[n] != arr[i]:
                answer.append(arr[i])
        else:
            answer.append(arr[i]) 
        
    return answer