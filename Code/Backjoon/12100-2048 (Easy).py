# 레퍼런스 코드 (훗날 직접 구현할 것)

import copy

## 가장 큰 값 업데이트하기
def find_max(array):
    global maxv
    for i in range(N):
        for j in range(N):
            if maxv < array[i][j]: 
                maxv = array[i][j]


## 왼쪽으로 이동
def move_left(board):
    for i in range(N):
        p = 0
        x = 0
        for q in range(N):
            if board[i][q] == 0: continue # 값이 0 이라면 건너뛴다
            if x == 0:                    # 기존에 담고있던 값이 없다면
                x = board[i][q]           # x에 값을 할당
            else:                         # 기존에 담고있는 값이 있다면
                if x == board[i][q]:      # 동일한 값이라면
                    board[i][p] = 2*x     # i번째 자리에 2x를 업데이트
                    p = p + 1             # p 한칸 이동
                    x = 0                 # x 초기화
                else:                     # 다른 값이라면
                    board[i][p] = x       # i번째 자리에 x값 입력
                    p = p + 1             # p 한칸 이동
                    x = board[i][q]       # 새로운 x값
            board[i][q] = 0               # 나중에 번거로운 작업을 없애주기 위한것
        if x != 0: board[i][p] = x        # 마지막으로 고려해줘야 할것
    return board


## 오른쪽으로 이동
def move_right(board):
    for i in range(N):
        p = N-1
        x = 0
        for q in range(N-1, -1, -1):
            if board[i][q] == 0: continue # 값이 0 이라면 건너뛴다
            if x == 0:                    # 기존에 담고있던 값이 없다면
                x = board[i][q]           # x에 값을 할당
            else:                         # 기존에 담고있는 값이 있다면
                if x == board[i][q]:      # 동일한 값이라면
                    board[i][p] = 2*x     # i번째 자리에 2x를 업데이트
                    p = p - 1             # p 한칸 이동
                    x = 0                 # x 초기화
                else:                     # 다른 값이라면
                    board[i][p] = x       # i번째 자리에 x값 입력
                    p = p - 1             # p 한칸 이동
                    x = board[i][q]       # 새로운 x값
            board[i][q] = 0               # 나중에 번거로운 작업을 없애주기 위한것
        if x != 0: board[i][p] = x        # 마지막으로 고려해줘야 할것
    return board


## 위쪽으로 이동
def move_up(board):
    for i in range(N):
        p = 0
        x = 0
        for q in range(N):
            if board[q][i] == 0: continue # 값이 0 이라면 건너뛴다
            if x == 0:                    # 기존에 담고있던 값이 없다면
                x = board[q][i]           # x에 값을 할당
            else:                         # 기존에 담고있는 값이 있다면
                if x == board[q][i]:      # 동일한 값이라면
                    board[p][i] = 2*x     # i번째 자리에 2x를 업데이트
                    p = p + 1             # p 한칸 이동
                    x = 0                 # x 초기화
                else:                     # 다른 값이라면
                    board[p][i] = x       # i번째 자리에 x값 입력
                    p = p + 1             # p 한칸 이동
                    x = board[q][i]       # 새로운 x값
            board[q][i] = 0               # 나중에 번거로운 작업을 없애주기 위한것
        if x != 0: board[p][i] = x        # 마지막으로 고려해줘야 할것
    return board


## 아래쪽으로 이동
def move_down(board):
    for i in range(N):
        p = N-1
        x = 0
        for q in range(N-1, -1, -1):
            if board[q][i] == 0: continue # 값이 0 이라면 건너뛴다
            if x == 0:                    # 기존에 담고있던 값이 없다면
                x = board[q][i]           # x에 값을 할당
            else:                         # 기존에 담고있는 값이 있다면
                if x == board[q][i]:      # 동일한 값이라면
                    board[p][i] = 2*x     # i번째 자리에 2x를 업데이트
                    p = p - 1             # p 한칸 이동
                    x = 0                 # x 초기화
                else:                     # 다른 값이라면
                    board[p][i] = x       # i번째 자리에 x값 입력
                    p = p - 1             # p 한칸 이동
                    x = board[q][i]       # 새로운 x값
            board[q][i] = 0               # 나중에 번거로운 작업을 없애주기 위한것
        if x != 0: board[p][i] = x        # 마지막으로 고려해줘야 할것
    return board


def dfs(dfs_board, n): # 이동횟수(n)
    if n == 5:
        find_max(dfs_board)
        return
    dfs(move_left(copy.deepcopy(dfs_board)), n+1)
    dfs(move_right(copy.deepcopy(dfs_board)), n+1)
    dfs(move_up(copy.deepcopy(dfs_board)), n+1)
    dfs(move_down(copy.deepcopy(dfs_board)), n+1)


N = int(input())
maxv = 0
map_board = [list(map(int, input().split())) for _ in range(N)]
dfs(map_board, 0)
print(maxv)

# 구현 + 백트래킹임을 머리론 인지했지만 차마 손을 움직일 수 없었다.
# 방대한 스케일에 우선 레퍼런스를 참고하고 추후 내 코드로 구현하겠다.