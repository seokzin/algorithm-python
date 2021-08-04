import sys
input= sys.stdin.readline

n, m = map(int, input().split())
memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
dp = [[0] * (sum(cost)+1) for _ in range(n+1)]  # 앱, 비용을 축으로 가진 2차원 dp
res = sum(cost)

for i in range(1, n+1):
    for j in range(sum(cost)+1):
        if cost[i] > j:  # 비용 초과로 앱 활성화 불가
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i]] + memory[i])

        if dp[i][j] >= m:
            res = min(res, j)

print(res)

# 0-1 Knapsack Problem
# 손코딩으로 이해해보려니 잘 안된다. 나중에 다시 돌아보자