# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    basket = []
    
    for i in moves:
        col = [row[i-1] for row in board]
        l = next((item for item in col if item != 0), 0)

        if l != 0:
            for row in board:
                if row[i-1] == l:
                    row[i-1] = 0
                    break
        print(l)
        if len(basket) > 0 and l == basket[len(basket)-1] and l != 0:
            answer+=2
            basket.pop()
        else:
            basket.append(l)
    
    return answer
