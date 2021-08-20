def check():
    for i in range(1, 10):
        if dp[i][9] != 45 * i:
            return 0
        if dp[9][i] != 45 * i:
            return 0
    
    for j in (3, 6, 9):  # 33검증
        for k in (3, 6, 9):
            if dp[k][j] - dp[k-3][j] - dp[k][j-3] + dp[k-3][j-3] != 45:
                return 0 

    return 1

for tc in range(1, int(input())+1):
    board = [list(map(int, input().split())) for _ in range(9)]
    dp = [[0 for _ in range(10)] for _ in range(10)]

    for i in range(9):
        for j in range(9):
            dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - dp[i][j] + board[i][j]

    print(f'#{tc}', check())

# 부분합을 통해 O(N) 풀이