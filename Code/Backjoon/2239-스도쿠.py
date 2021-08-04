def find_empty():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j

    return None, None

def is_valid(col, row, x):
    # 가로 축 점검
    for i in range(9):
        if board[col][i] == x:
            return False

    # 세로 축 점검
    for i in range(9):
        if board[i][row] == x:
            return False

    # 3x3 박스 점검
    col_mid = col//3 * 3  # 3x3 의 중앙
    row_mid = row//3 * 3
    for i in range(3):
        for j in range(3):
            if board[col_mid+i][row_mid+j] == x:
                return False

    return True

def solve():
    col, row = find_empty()

    if col is None:
        return True

    else:
        for i in range(1, 10):
            if is_valid(col, row, i):
                board[col][row] = i

                if solve():
                    return True

                board[col][row] = 0

        return False

board = []

for _ in range(9):
    line = list(map(int, input()))
    board.append(line)

solve()

for line in board:
    print(*line, sep='', end='\n')

# 답이 나오지 않을 땐 백 트래킹!
# 사실 solve 파트의 백트래킹 방식이 조금 이해가 어려웠다
# 근데 Pypy에서만 시간초과가 안뜬다.. 이런
# 나중에 다시보자