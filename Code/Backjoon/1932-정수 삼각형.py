n = int(input())

dp = []

for _ in range(n):
  dp.append(list(map(int, input().split())))

for i in range(1, n):
  for j in range(i+1):
    if j == 0:
      dp[i][j] += dp[i-1][j]
    elif j == i:
      dp[i][j] += dp[i-1][j-1]
    else:
      dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[-1]))

# 기본적인 dp 문제..