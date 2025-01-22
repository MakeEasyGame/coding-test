def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        bin_map = bin(arr1[i] | arr2[i])[2:].zfill(n)
        answer.append(bin_map.replace('1', '#').replace('0', ' '))
    
    return answer