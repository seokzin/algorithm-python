for tc in range(1, int(input())+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0]*(N+1) for _ in range(N)]

    for i in range(1, N):
        dp[0][i] = min(dp[1][i-1], dp[2][i-1]) + arr[0][i]
        dp[1][i] = min(dp[0][i-1], dp[2][i-1]) + arr[1][i]
        dp[2][i] = min(dp[0][i-1], dp[1][i-1]) + arr[2][i]

    print(dp)
# 완전 DP라 생각했습니다.