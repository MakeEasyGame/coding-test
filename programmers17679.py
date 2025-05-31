# [1차] 프렌즈4블록

def solution(m, n, board):
    board = [list(row) for row in board]
    removed = 0
    while True:
        remove = set()
        for i in range(m - 1): # 2x2 블럭을 탐색하기 위한 세로줄
            for j in range(n - 1): # 2x2 블럭을 탐색하기 위한 가로줄
                block = board[i][j] # 현재 블럭
                if block == ' ': # 블럭이 비어있다면
                    continue # 넘어가기
                if block == board[i][j+1] == board[i+1][j] == board[i+1][j+1]: # 2x2블럭이 모두 같은지 확인
                    remove.update([(i, j), (i, j+1), (i+1, j), (i+1, j+1)]) # 지울 리스트에 추가
        if not remove: # 지울게 없다면
            break # 끝내기
        for x, y in remove: # 지울 리스트를 탐색
            board[x][y] = ' ' # 지우기
        removed += len(remove) # 지워진 블럭을 카운트
        for col in range(n): # 가로줄 탐색
            stack = [] # 한 줄에 쌓인 스택
            for row in range(m-1, -1, -1): # 바닥에서부터 한 칸씩 탐색
                if board[row][col] != ' ': # 현재 블럭이 비어있지않다면
                    stack.append(board[row][col]) # 스택에 담기
            for row in range(m-1, -1, -1): # 다시 바닥에서부터 탐색
                board[row][col] = stack.pop(0) if stack else ' ' # 스택이 비어있지않으면 삭제하고 보드에 넣어주기, 그렇지 않으면 빈칸으로 냅두기

    return removed
