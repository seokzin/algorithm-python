n = int(input())

dp = [] 


for _ in range(n):
  dp.append(list(map(int, input().split())))

for i in range(1, n):
  dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
  dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]
  dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]

print(min(dp[n-1]))

# dp 값을 대체하는 방식이 낫나? rgb와 dp 데이터를 개별 분리하는 게 낫나?