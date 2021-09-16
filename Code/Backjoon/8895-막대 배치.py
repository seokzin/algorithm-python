dp = [[[0]*21 for _ in range(21)] for _ in range(21)]

dp[1][1][1] = 1

for i in range(2, 21):
    for l in range(1, i+1):
        for r in range(1, i+1):
            dp[i][l][r] = dp[i-1][l-1][r] + dp[i-1][l][r-1] + (i-2)*dp[i-1][l][r]

for _ in range(int(input())):
    n, l, r = map(int, input().split())
    print(dp[n][l][r])

# 사실 점화식은 이해가 돼도 문제 자체가 이해가 안됐음