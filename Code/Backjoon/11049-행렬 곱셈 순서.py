import sys
input = sys.stdin.readline
MAX = 2**31

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(1, n):  # 대각선 탐색 구현
    for j in range(n-i):
        x = j+i
        dp[j][x] = MAX

        for k in range(j, x):
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k+1][x] + s[j][0]*s[k][1]*s[x][1])

print(dp[0][n-1])

# 대각선 DP 계산 방식은 이해는 했다만 실제로 내가 구현할 수 있을까?
# 또한 행렬의 합이 DP 구조임을 실제로 이해할 수 있을까? 다시 풀자
# 또 파이썬은 시간초과가 뜬다. 까탈스러운 문제다