dp = [0, 1, 3]

for i in range(3, 1001):
    dp.append(dp[i-1] + 2*dp[i-2])

print(dp[int(input())] % 10007)

# Tabulation
# 디테일에서 여러번 틀렸다. 경계값 조심