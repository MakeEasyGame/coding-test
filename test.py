# 파일명 정렬

def solution(m, n, board):
    board = [list(row) for row in board]
    removed = 0
    while True:
        remove = set()
        for i in range(m - 1):
            for j in range(n - 1):
                block = board[i][j]
                if block == ' ':
                    continue
                if block == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    remove.update([(i, j), (i, j+1), (i+1, j), (i+1, j+1)])
        if not remove:
            break
        for x, y in remove:
            board[x][y] = ' '
        removed += len(remove)
        for col in range(n):
            stack = []
            for row in range(m-1, -1, -1):
                if board[row][col] != ' ':
                    stack.append(board[row][col])
            for row in range(m-1, -1, -1):
                board[row][col] = stack.pop(0) if stack else ' '

    return removed
