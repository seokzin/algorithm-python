n = int(input())
dp = [0, 1]

for i in range(2, n+1):
    cnt = 50000

    for j in range(1, int(i**0.5)+1):
        cnt = min(cnt, dp[i - (j**2)])

    dp.append(cnt+1)

print(dp[-1])

# bottom-up DP - 제곱 단위로 탐색
# Python3 시간 초과